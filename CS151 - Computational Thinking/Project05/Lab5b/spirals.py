'''Veer Khosla
CS151 A
3/17/23
Lab5 B
Spiral Art
spirals.py'''

import turtle as t
import random as r
import sys

def draw_screen(width, height, title, color = 'white'):
    '''makes screen of any dimensions, title, and background color'''
    screen = t.Screen()
    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor(color)
    return screen


def make_turtle(shape='turtle', penColor='white'):
    '''makes turtle of any type and color'''
    turt = t.Turtle()
    turt.shape(shape)
    turt.pencolor(penColor)
    return turt


def draw_spiral(discontinuous = False, jitter = False):
    '''draws different kinds of spirals, specified with arguments, on a screen object with a black background.'''
    screen = draw_screen(800, 700, 'Spiral Art', 'black')

    widthMax = screen.window_width() / 2
    widthMin = -screen.window_width() / 2
    heightMax = screen.window_height() / 2
    heightMin = -screen.window_height() / 2

    turtles = []  # create a list to hold the turtles
    for i in range(6):
        spiralTurt = make_turtle('classic', 'white')
        spiralTurt.speed(0)
        turtles.append(spiralTurt)  # add the turtle to the list

    heading = [0, 60, 120, 180, 240, 300]

    numSpirals = 0
    while numSpirals < 40:
        for i, turtle in enumerate(turtles):
            randColor = r.random(), r.random(), r.random()
            turtle.pencolor(randColor)
            turtle.pensize(4)
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.setheading(heading[i])

            if discontinuous == False:
                # REGULAR SPIRAL
                if jitter == False:
                    while widthMin <= turtle.xcor() <= widthMax and heightMin <= turtle.ycor() <= heightMax:
                        turtle.circle(widthMax, 30)
                else:
                    headingJitter = heading[i] - 20
                    while widthMin <= turtle.xcor() <= widthMax and heightMin <= turtle.ycor() <= heightMax:
                        turtle.setheading(headingJitter)
                        turtle.circle(75, 100)
                        posJitter = turtle.pos()
                        turtle.penup()
                        turtle.goto(posJitter)
                        turtle.setheading(heading[i])
                        turtle.fd(35)
                        turtle.pendown()
                        headingJitter = heading[i] + 20

            else:
                # DISCONTINOUS SPIRAL:
                    while widthMin <= turtle.xcor() <= widthMax and heightMin <= turtle.ycor() <= heightMax:
                        turtle.pencolor(randColor)
                        turtle.fd(25)
                        turtle.left(3)
                        turtle.pencolor('black')
                        turtle.fd(25)
                        turtle.left(3)    

            heading[i] += 2
        numSpirals += 1


def sys_args():
    '''takes system argument to call function draw_spiral. Specifies different types of spirals for different inputs.'''
    if sys.argv[1] == 'regular':
        draw_spiral()
    elif sys.argv[1] == 'discontinuous':
        draw_spiral(True, False)
    elif sys.argv[1] == 'jitter':
        draw_spiral(False, True)
    else:
        print('ERROR: not a spiral type. Please enter: "regular", "discontinuous", or "jitter" for the desired spiral type')
        t.bye()

if __name__ == '__main__':
    sys_args()
    t.exitonclick()
