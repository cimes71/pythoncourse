from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height= 600)
screen.tracer(0)
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.move()
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()



screen.exitonclick()