import turtle
import time
import random
from _tkinter import TclError


ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")
BACKGROUND_COLOR = "#ffffff"
BALL_COLOR = "green"
RIGHT_PADDLE_COLOR = "blue"
LEFT_PADDLE_COLOR = "red"
PARTITION_COLOR = "#37ad2d"
SCORE_COLOR = "orange"


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.shape("circle")
        self.penup()
        self.move_x = 15
        self.move_y = 15
        self.move_speed = 0.1
        self.spawn()
    

    def move(self):
        new_x_cord = self.xcor() - self.move_x
        new_y_cord = self.ycor() - self.move_y
        self.goto(x=new_x_cord, y=new_y_cord)
    

    def bounce_y(self):
        self.move_y *= -1
        self.move_speed *= 0.9


    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9


    def spawn(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        moving_list = [-1, 1]
        self.move_x *= random.choice(moving_list)
        self.move_y *= random.choice(moving_list)


class Paddle(turtle.Turtle):

    def __init__(self, position, paddle_color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(paddle_color)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        self.move_x = 1
        self.move_y = 1
        self.moving_up = False
        self.moving_down = False
    

    def move(self):
        if self.moving_up:
            self.move_up()
        if self.moving_down:
            self.move_down()
    
    
    def move_up(self):
        new_y_cord = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y_cord)
    

    def move_down(self):
        new_y_cord = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_cord)
    

    def start_moving_up(self):
        self.moving_up = True
    

    def stop_moving_up(self):
        self.moving_up = False
    

    def start_moving_down(self):
        self.moving_down = True
    

    def stop_moving_down(self):
        self.moving_down = False


class Partition(turtle.Turtle):

    def __init__(self, initial_position, final_position):
        super().__init__()
        self.shape("square")
        self.color(PARTITION_COLOR)
        self.shapesize(stretch_len=1, stretch_wid=3)
        self.penup()
        self.goto(initial_position)
        while self.pos() < final_position:
            self.goto(self.xcor(), self.ycor() + 50)
            self.stamp()
            self.goto(self.xcor(), self.ycor() + 50)


class Scoreboard(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.color(SCORE_COLOR)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.hideturtle()
        self.speed("fastest")
        self.score = -1
        self.goto(position)
        self.increse_score()
    

    def increse_score(self):
        self.score += 1
        self.clear()
        self.write(arg=self.score, align=ALIGNMENT, font=FONT)


def main():
    try:
        screen = turtle.Screen()
        screen.setup(width=1000, height=700)
        screen.title("Pong Ball")
        screen.bgcolor(BACKGROUND_COLOR)


        score_limit = screen.textinput(title="Choose Score Limit", prompt="What should be the limit of scores? ")


        screen.tracer(0)


        right_paddle = Paddle((480, 0), RIGHT_PADDLE_COLOR)
        left_paddle = Paddle((-490, 0), LEFT_PADDLE_COLOR)
        ball = Ball()
        right_side = Scoreboard((250, 280))
        left_side = Scoreboard((-250, 280))
        partition = Partition((0, -500), (0, 500))


        game_over = False

        while not game_over:

            if right_side.score == int(score_limit) or left_side.score == int(score_limit):
                game_over = True
            
            if game_over:
                notice = turtle.Turtle()
                notice.hideturtle()
                notice.penup()
                notice.color("#f4a172")
                notice.speed("fastest")
                notice.goto(0, 0)
                notice.write("Game Over", align="center", font=("Arial", 36, "normal"))

            screen.update()
            time.sleep(ball.move_speed)

            screen.listen()
            screen.onkeypress(key="Up", fun=right_paddle.start_moving_up)
            screen.onkeyrelease(key="Up", fun=right_paddle.stop_moving_up)
            screen.onkeypress(key="Down", fun=right_paddle.start_moving_down)
            screen.onkeyrelease(key="Down", fun=right_paddle.stop_moving_down)
            screen.onkeypress(key="w", fun=left_paddle.start_moving_up)
            screen.onkeyrelease(key="w", fun=left_paddle.stop_moving_up)
            screen.onkeypress(key="s", fun=left_paddle.start_moving_down)
            screen.onkeyrelease(key="s", fun=left_paddle.stop_moving_down)

            right_paddle.move()
            left_paddle.move()

            if ball.xcor() >= 60:
                ball.color(RIGHT_PADDLE_COLOR)
            elif ball.xcor() <= -60:
                ball.color(LEFT_PADDLE_COLOR)
            else:
                ball.color(BALL_COLOR)

            if ball.ycor() >= 340 or ball.ycor() <= -330:
                ball.bounce_y()
            
            if (
                (abs(right_paddle.xcor() - ball.xcor()) <= 20 and abs(right_paddle.ycor() - ball.ycor()) <= 60) or
                (abs(left_paddle.xcor() - ball.xcor()) <= 20 and abs(left_paddle.ycor() - ball.ycor()) <= 60)
                ):
                ball.bounce_x()
            
            ball.move()

            if ball.xcor() > 500:
                ball.spawn()
                left_side.increse_score()
            elif ball.xcor() < -500:
                ball.spawn()
                right_side.increse_score()


        screen.exitonclick()
    
    except TclError:
        pass
    except turtle.Terminator:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()