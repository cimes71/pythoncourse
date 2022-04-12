from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
screen.tracer(0)

s = []

scoreboard = ScoreBoard()


while game_is_on:

   screen.update()
   time.sleep(.1)
   snake.move()
   if snake.head.distance(food)  < 15:
      print("nom nom nom")
      food.refresh()
      snake.extend()
      scoreboard.update_score()
   if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
           snake.head.ycor() > 280 or snake.head.ycor() < -280:
      game_is_on = False
      scoreboard.game_over()
   for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
         game_is_on = False
         scoreboard.game_over()















screen.exitonclick()