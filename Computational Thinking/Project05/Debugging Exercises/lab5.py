'''Veer Khosla
CS151 A
3/9/23
lab5.py
debugging + fixing coding style
'''

import turtle

#defines turtle objects
x = turtle.Turtle()
y = turtle.getscreen()


#sets color of screen, and color, speed, and movement of turtle object.
#Also sets initial value of pensize
pen_size = 1
speedTurtle = 0

x.speed(speedTurtle)
y.bgcolor('black')
x.color('white')
x.forward(1)



#makes squares which rotate by 91 degrees on each iteration (300 total).
#changes the color of turtle based on the number of iterations.
for z in range(300):
    x.forward(z * 1.5)
    x.left(91)
    pen_size *= 1.004
    x.pensize(pen_size)
    if z < 101:
        tammy = ((z/100), 0, 0)
    elif z < 201:
        tammy = (1 - ( (z-100) / 100 ), ( (z-100) / 100 ), 0)
    else:
        tammy = (1 - ( (z-200) / 100 ), 1 - ( (z-200) / 100 ), ( (z-200) / 100 ))
    x.color(tammy)


x.forward(300 * 0.5)
turtle.hideturtle()
x.hideturtle()
turtle.exitonclick()