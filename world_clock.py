import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import pytz
from threading import Thread
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim



BACKGROUND_COLOR = "#218ed1"



class WorldClock:
    
    def __init__(self, window: tk.Tk):
        self.window = window
        self.window.title("World Clock")
        self.window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

        self.clocks = []
        self.clock_number = 0

        self.city_add_entry = ttk.Entry(self.window, width=30, font=("Arial", 15, "italic"))
        self.city_add_entry.grid(row=0, column=0, columnspan=2)
        self.add_button = ttk.Button(self.window, text="Add City", width=54, command=self.add_city_in_background)
        self.add_button.grid(row=1, column=0, pady=10, columnspan=2)

        self.scroll_canvas = tk.Canvas(self.window, width=640, height=400, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0)
        self.scroll_canvas.grid(row=2, column=0, columnspan=2)

        self.scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.scroll_canvas.yview)
        self.scrollbar.grid(row=2, column=2, sticky="ns")

        self.clocks_frame = tk.Frame(self.scroll_canvas, bg=BACKGROUND_COLOR)
        self.scroll_canvas.create_window((0, 0), window=self.clocks_frame, anchor="nw")
        self.scroll_canvas.config(yscrollcommand=self.scrollbar.set)

        self.clocks_frame.bind("<Configure>", self.update_scroll_region)

        self.update_clocks()

    
    def update_scroll_region(self, event=None):
        self.scroll_canvas.config(scrollregion=self.scroll_canvas.bbox("all"))

    
    def get_timezone_from_city(self, city_name):
        try:
            geolocator = Nominatim(user_agent="city-time-converter")
            location = geolocator.geocode(city_name)

            if location:
                latitude, longitude = location.latitude, location.longitude
                tz_finder = TimezoneFinder()
                return tz_finder.timezone_at(lat=latitude, lng=longitude)
            return None
        
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Error: {e}")
            return None

    
    def add_city_in_background(self):
        city_name = self.city_add_entry.get().strip()
        if city_name and not any(clock["city"].lower() == city_name.lower() for clock in self.clocks):
            Thread(target=self.add_city_worker, args=(city_name,)).start()
        else:
            message = f"City '{city_name}' is already added or invalid."
            messagebox.showwarning(title="Invalid City", message=message, )

    
    def add_city_worker(self, city_name):
        timezone = self.get_timezone_from_city(city_name)
        if timezone:
            self.window.after(0, lambda: self.add_city_to_grid(city_name, timezone))

    
    def add_city_to_grid(self, city_name, timezone):
        row = self.clock_number // 2
        column = self.clock_number % 2

        canvas = tk.Canvas(self.clocks_frame, width=300, height=150, bg="white", highlightthickness=0, bd=0)
        canvas.grid(row=row, column=column, padx=10, pady=10)

        city_time = datetime.now(pytz.timezone(timezone))
        self.clocks.append({"city": city_name.capitalize(), "timezone": timezone, "canvas": canvas, "time": city_time})

        self.clock_number += 1

    
    def update_clocks(self):
        for clock in self.clocks:
            clock["time"] += timedelta(seconds=1)
            clock["canvas"].delete("all")
            clock["canvas"].create_text(150, 60, text=clock["time"].strftime("%H:%M:%S"), font=("Arial", 48), fill="black")
            clock["canvas"].create_text(150, 120, text=f"{clock['city']} ({clock['timezone']})", font=("Arial", 16), fill="gray")

        self.window.after(1000, self.update_clocks)



if __name__ == "__main__":
    root = tk.Tk()
    world_clock = WorldClock(root)
    root.mainloop()
