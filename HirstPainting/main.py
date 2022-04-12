import random
import turtle
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")

# colors = colorgram.extract('image.jpg', 30)
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (223, 137, 176), (143, 108, 57),
              (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (119, 191, 139),
              (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210),
              (229, 168, 185), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 101

for count in range(1, num_of_dots):
    tim.dot(20, choice(color_list))
    tim.forward(50)
    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()
Screen().exitonclick()





# def draw_dots(x_pos, y_pos):
#     for r in range(10):
#         m = 0
#         while m <= 10:
#             tim.dot(20, choice(color_list))
#             tim.forward(50)
#             m += 1
#
#         y_pos = y_pos + 50
#         tim.setposition(x_pos,y_pos)
#
# x_pos = -250
# y_pos = -250
# tim.setposition(x_pos, y_pos)
# draw_dots(x_pos, y_pos)
# Screen().exitonclick()