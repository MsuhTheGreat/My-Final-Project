import turtle
import time
import time
import random
from _tkinter import TclError


# Snake class constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
INCREASING_SPEED = 0.25
# Food class constants
SPEED = 1
# Scoreboard class constants
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        segment = turtle.Turtle(shape="square")
        # segment.shapesize(stretch_wid=0.5, stretch_len=1)
        segment.penup()
        segment.color("red")
        segment.goto(position)
        self.segments.append(segment)


    def extend_tail(self):
        self.add_segment(self.segments[-1].pos())


    def go_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)


    def go_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)


    def go_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)


    def go_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)


    def move_snake(self, screen):
        i = -1

        while i > -len(self.segments):
            second_segment = self.segments[i]
            i -= 1
            first_segment = self.segments[i]
            second_segment.goto(first_segment.pos())

        screen.listen()
        screen.onkey(key="Up", fun=self.go_up)
        screen.onkey(key="Down", fun=self.go_down)
        screen.onkey(key="Right", fun=self.go_right)
        screen.onkey(key="Left", fun=self.go_left)

        self.segments[0].forward(MOVING_DISTANCE)


    def touch_wall(self):
        if (self.head.xcor() > 475) or (self.head.xcor() <= -490) or (self.head.ycor() > 345) or (self.head.ycor() < -330):
            return True


    def touch_tail(self):
        cond = False
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 5:
                cond = True
        return cond
    

    def increse_speed(self):
        global MOVING_DISTANCE
        MOVING_DISTANCE += INCREASING_SPEED
    

    def change_color(self, colour):
        for segment in self.segments:
            segment.color(colour)
        self.segments[-1].color(colour)


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.colors = ['indigo', 'blue',
                       'yellow', 'orange']
        self.directions = [0, 90, 180, 270]
        # self.shape("turtle")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()


    def move_food(self):
        self.forward(SPEED)


    def cross_wall(self):
        return bool(
            self.xcor() >= 505 or
            self.xcor() <= -505 or
            self.ycor() >= 360 or
            self.ycor() <= -360
                    )


    def refresh(self):
        self.colour = random.choice(self.colors)
        self.setheading(random.choice(self.directions))
        self.color(self.colour)
        x_cord = random.randint(-450, 450)
        y_cord = random.randint(-300, 300)
        self.goto(x=x_cord, y=y_cord)


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=320)
        self.score = 0
        self.update_score()


    def update_score(self):
        text = f"Your current score = {self.score}"
        self.write(arg=text, align=ALIGNMENT, font=FONT)


    def display_game_over(self):
        self.goto(0, 0)
        text = "Game Over"
        self.write(arg=text, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


    def decrease_score(self):
        self.score -= 1
        self.clear()
        self.update_score()


def main():
    try:
        screen = turtle.Screen()
        screen.setup(width=1000, height=700)
        screen.bgcolor("green")
        screen.title("The Greedy Snake")
        screen.tracer(0)

        snake = Snake()
        food = Food()
        scoreboard = Scoreboard()

        game_over = False
        while not game_over:
            time.sleep(0.05)
            screen.update()
            # food.move_food()

            if snake.touch_wall() or snake.touch_tail():
                game_over = True

            if food.cross_wall():
                food.refresh()
                scoreboard.decrease_score()

            if snake.head.distance(food) <= 15:
                food.refresh()
                # snake.change_color(food.colour)
                scoreboard.increase_score()
                snake.extend_tail()
                snake.increse_speed()

            else:
                snake.move_snake(screen=screen)

        if game_over:
            scoreboard.display_game_over()

        screen.exitonclick()
    
    except TclError:
        pass
    except turtle.Terminator:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()