"""randomwalker.py"""

import turtle
import random

count = 0
while count <51:
    count += 1
    if (turtle.xcor() >-300 and turtle.xcor() <300) and\
       (turtle.ycor() >-300 and turtle.ycor() <300):
        turtle.forward(random.randint(30,100))
        turtle.right(random.randint(0,360))
    else:
        turtle.right(180)
        turtle.forward(300)    