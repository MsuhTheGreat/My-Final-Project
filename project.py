import tkinter as tk
from quiz import Quiz
from world_clock import WorldClock
import pong
import snake
import turtle_race
import turtle_road_crossing
from multiprocessing import Process
from PIL import Image, ImageTk


QUIZ_IMAGE_PATH = r"final_project\images\quiz image.png"
WORLD_CLOCK_IMAGE_PATH = r"final_project\images\clock image.png"
OLD_GAMES_IMAGE_PATH = r"final_project\images\old games image.png"
PONG_IMAGE_PATH = r"final_project\images\pong game image.png"
SNAKE_IMAGE_PATH = r"final_project\images\snake game image.png"
TURTLE_RACE_IMAGE_PATH = r"final_project\images\turtle race image.png"
TURTLE_ROAD_CROSS_IMAGE_PATH = r"final_project\images\turtle road crossing image.png"

IMAGE_HEIGHT_PX = 300
IMAGE_WIDTH_PX = 250


class Main_Window:
    
    def __init__(self, window:tk.Tk) -> None:
        self.window = window
        self.window.title("Main Window")
        self.window.config(padx=100, pady=50)
        
        self.quiz_image = ImageTk.PhotoImage(Image.open(QUIZ_IMAGE_PATH).resize((IMAGE_WIDTH_PX, IMAGE_HEIGHT_PX)))
        self.world_clock_image = ImageTk.PhotoImage(Image.open(WORLD_CLOCK_IMAGE_PATH).resize((IMAGE_WIDTH_PX, IMAGE_HEIGHT_PX)))
        self.old_games_image = ImageTk.PhotoImage(Image.open(OLD_GAMES_IMAGE_PATH).resize((IMAGE_WIDTH_PX, IMAGE_HEIGHT_PX)))

        self.quiz_button = tk.Button(self.window, image=self.quiz_image, text="Quiz", command=self.play_quiz)
        self.quiz_button.grid(row=0, column=0, padx=50, pady=30)

        self.world_clock_button = tk.Button(self.window, image=self.world_clock_image, text="World Clock", command=self.use_world_clock)
        self.world_clock_button.grid(row=0, column=1, padx=50, pady=30)

        self.games_button = tk.Button(self.window, image=self.old_games_image, text="Games", command=self.load_old_games_window)
        self.games_button.grid(row=1, column=0, columnspan=2 ,padx=100, pady=30)


    def load_old_games_window(self):
        try:
            top_window = tk.Toplevel(self.window)
            Old_Games_Window(top_window)
        except Exception as e:
            print(f"Error occurred: {e}")

    
    def play_quiz(self):
        try:
            top_window = tk.Toplevel(self.window)
            Quiz(top_window)
        except Exception as e:
            print(f"Error occurred: {e}")


    def use_world_clock(self):
        try:
            top_window = tk.Toplevel(self.window)
            WorldClock(top_window)
        except Exception as e:
            print(f"Error occurred: {e}")


class Old_Games_Window:

    def __init__(self, window:tk.Tk) -> None:
        self.window = window
        self.window.title("Old Games Window")
        self.window.config(padx=100, pady=50)
        
        self.pong_image = ImageTk.PhotoImage(Image.open(PONG_IMAGE_PATH).resize((IMAGE_WIDTH_PX, IMAGE_HEIGHT_PX)))
        self.snake_image = ImageTk.PhotoImage(Image.open(SNAKE_IMAGE_PATH).resize((IMAGE_WIDTH_PX, IMAGE_HEIGHT_PX)))
        self.turtle_race_image = ImageTk.PhotoImage(Image.open(TURTLE_RACE_IMAGE_PATH).resize((IMAGE_WIDTH_PX, IMAGE_HEIGHT_PX)))
        self.turtle_road_crossing_image = ImageTk.PhotoImage(Image.open(TURTLE_ROAD_CROSS_IMAGE_PATH).resize((IMAGE_WIDTH_PX, IMAGE_HEIGHT_PX)))

        self.turtle_road_cossing_game_button = tk.Button(self.window, image=self.turtle_road_crossing_image, text="Turtle Road Crossing Game", command=self.play_turtle_road_crossing_game)
        self.turtle_road_cossing_game_button.grid(row=0, column=0, padx=50, pady=30)

        self.snake_game_button = tk.Button(self.window, image=self.snake_image, text="Snake Game", command=self.play_snake_game)
        self.snake_game_button.grid(row=0, column=1, padx=50, pady=30)

        self.pong_game_button = tk.Button(self.window, image=self.pong_image, text="Pong Game", command=self.play_pong)
        self.pong_game_button.grid(row=1, column=0, padx=50, pady=30)

        self.turtle_racing_game_button = tk.Button(self.window, image=self.turtle_race_image, text="Turtle Racing Game", command=self.play_turtle_racing_game)
        self.turtle_racing_game_button.grid(row=1, column=1, padx=50, pady=30)

        
    def play_game(self, target):
        self.current_process = Process(target=target)
        self.current_process.start()
    

    def play_pong(self):
        self.play_game(pong.main)


    def play_snake_game(self):
        self.play_game(snake.main)


    def play_turtle_racing_game(self):
        self.play_game(turtle_race.main)


    def play_turtle_road_crossing_game(self):
        self.play_game(turtle_road_crossing.main)


def main():
    window = tk.Tk()
    Main_Window(window)
    window.mainloop()


def start_playing_quiz():
    return "Yeah! I am playing quiz!"


def start_using_world_clock():
    return "Oh! This world clock is very useful!"


def start_playing_old_games():
    return "Finally! Some good old games to play!"


if __name__ == "__main__":
    main()
