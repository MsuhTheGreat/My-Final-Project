import random
import turtle
import time
from _tkinter import TclError


FONT = ("Arial", 30, "normal")


class Car_Manager:

    def __init__(self):
        self.car_list = []
        self.car_speed = 10
        self.i = 6
    
    
    def create_car(self):
        i = random.randint(1, self.i)
        if i == 1:
            color_list = ["red", "yellow", "orange", "green", "blue", "purple"]
            car = turtle.Turtle(shape="square")
            car.color(random.choice(color_list))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.goto(x=510, y=random.randint(-280, 280))
            self.car_list.append(car)
    

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset_position()
        self.moving_speed = 10
        self.moving_up = False
        self.moving_down = False
    
    
    def start_moving_up(self):
        self.moving_up = True
    
    
    def stop_moving_up(self):
        self.moving_up = False
    
    
    def start_moving_down(self):
        self.moving_down = True
    
    
    def stop_moving_down(self):
        self.moving_down = False

    
    def move(self):
        if self.moving_up:
            self.forward(self.moving_speed)
        if self.moving_down:
            self.backward(self.moving_speed)
        
    
    def reset_position(self):
        self.setheading(90)
        self.goto(0, -330)


class Stage(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.stage_no = 1
        self.color("coral")
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.write_stage()
    
    
    def broke_the_game(self):
        self.goto(0, 0)
        self.write(arg="Congrats! You broke the game! 🎉", align="center", font=FONT)

    
    def display_game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
    
    
    def write_stage(self):
        self.clear()
        self.write(arg=f"Stage: {self.stage_no}", align="center", font=FONT)


def main():
    try:
        screen = turtle.Screen()
        screen.title("Turtle Road Crossing")
        screen.bgcolor("#30e2db")
        screen.setup(width=1000, height=700)
        screen.tracer(0)

        tony = Player()
        car_manager = Car_Manager()
        stage = Stage()

        screen.listen()
        screen.onkeypress(key="Up", fun=tony.start_moving_up)
        screen.onkeyrelease(key="Up", fun=tony.stop_moving_up)
        screen.onkeypress(key="Down", fun=tony.start_moving_down)
        screen.onkeyrelease(key="Down", fun=tony.stop_moving_down)

        game_on = True
        while game_on:
            screen.update()
            time.sleep(0.1)
            for car in car_manager.car_list:
                if car.xcor() <= -500:
                    car.hideturtle()
                    indx = car_manager.car_list.index(car)
                    car_manager.car_list.pop(indx)
                if (abs(tony.xcor()-car.xcor()) < 30 and
                    abs(tony.ycor()-car.ycor()) < 20):
                    game_on = False
                    stage.display_game_over()
                    break
            if tony.ycor() >= 350:
                tony.reset_position()
                stage.stage_no += 1
                stage.write_stage()
                car_manager.car_speed += 10
                car_manager.i -= 1
            if stage.stage_no == 7:
                game_on = False
                stage.broke_the_game()
                break
            tony.move()
            car_manager.create_car()
            car_manager.move_cars()

        screen.exitonclick()
    
    except TclError:
        pass
    except turtle.Terminator:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()