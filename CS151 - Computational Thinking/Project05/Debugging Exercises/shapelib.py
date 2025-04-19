
import turtle
import math

window = turtle.getscreen()
tammy = turtle.Turtle()

def triangle(width, fill_color):
    tammy.color(fill_color)
    tammy.setheading(0)
    
    tammy.begin_fill()
    
    for i in range(3):
        tammy.forward(width)
        tammy.left(120)

    tammy.end_fill()


def rectangle(width, height, fill_color):
    tammy.color(fill_color)
    tammy.setheading(0)
    
    tammy.begin_fill()
    for i in range(2):
        tammy.forward(width)
        tammy.left(90)
        tammy.forward(height)
        tammy.left(90)
    tammy.end_fill()

# turtle.exitonclick()