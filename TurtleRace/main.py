
from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(500,400)
colors = ["red","orange","yellow",'green', "blue", "purple"]

user_bet = screen.textinput("Make your Bet", "Color of Turtle: ")
y_cord = -110
turtle_list = []

def check_winner(user_bet, turtle_color):
    if user_bet == turtle_color[0]:
        print(f"You've won {winner[1].upper()} wins the race!")
    else:
        print(f"You've lost {winner[1].upper()} wins the race!")

for t in range(len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    y_cord += 30
    new_turtle.goto(-230, y_cord)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            #check_winner(user_bet, turtle.color())
            winner = turtle.color()

            check_winner(user_bet, winner)
            is_race_on = False




















#tim = Turtle(shape="turtle")
#tim.penup()
#tim.goto(-230, -100)
#screen.listen()
#screen.onkey(key="a", fun=add_turtles)


screen.exitonclick()
