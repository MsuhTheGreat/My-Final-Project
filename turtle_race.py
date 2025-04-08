import turtle
import random
from tkinter import messagebox
from _tkinter import TclError


def main():
    try:
        screen = turtle.Screen()
        screen.setup(width=1000, height=700)
        screen.bgcolor("#a1a1a1")

        x_coordinates = 480
        y_coordinates = -350

        flag = turtle.Turtle(shape="square")
        flag.penup()

        for i in range(36):
            flag.goto(x=x_coordinates, y=y_coordinates)
            flag.color("white" if i % 2 == 0 else "black")
            flag.stamp()
            y_coordinates += 20

        x_coordinates = 460
        y_coordinates = -350

        for i in range(36):
            flag.goto(x=x_coordinates, y=y_coordinates)
            flag.color("black" if i % 2 == 0 else "white")
            flag.stamp()
            y_coordinates += 20


        prompt = "Which turtle will win the race?\n-Red\n-Blue\n-Green\n-Yellow\n-Orange\n-Purple"
        user_bet = screen.textinput(title="Place a bet", prompt=prompt).lower()


        x_coordinates = -480
        y_coordinates = 230

        turtle_dict = {
            "red": turtle.Turtle(shape="turtle"),
            "blue": turtle.Turtle(shape="turtle"),
            "green": turtle.Turtle(shape="turtle"),
            "yellow": turtle.Turtle(shape="turtle"),
            "orange": turtle.Turtle(shape="turtle"),
            "purple": turtle.Turtle(shape="turtle"),
        }

        colors = ["red", "blue", "green", "yellow", "orange", "purple"]
        random.shuffle(colors)

        race_over = False
        finish_line = 435

        while not race_over:
            for turtle_color in colors:
                tut = turtle_dict[turtle_color]
                tut.penup()
                tut.color(turtle_color)

                if tut.pos() == (0, 0):
                    tut.goto(x=x_coordinates, y=y_coordinates)
                    y_coordinates -= 100

                elif tut.pos()[0] > finish_line:

                    if turtle_color == user_bet:
                        message = f"Your {turtle_color.capitalize()} turtle won!"
                        messagebox.showinfo(title="End Of Game!", message=message)
                        
                    else:
                        message = f"Your turtle lost! {turtle_color.capitalize()} turtle won."
                        messagebox.showinfo(title="End Of Game!", message=message)
                        
                    race_over = True
                    break

                else:
                    tut.forward(random.randint(1, 11))


        screen.exitonclick()
    
    except TclError:
        pass
    except turtle.Terminator:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

