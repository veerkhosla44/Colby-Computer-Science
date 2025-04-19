'''Veer Khosla
CS151 A
Project 7
turtle_interpreter23.py'''

#Version 1

import turtle as t
import random as r

def drawString( dstring, distance, angle ):
    """ Interpret the characters in string dstring as a series
    of turtle commands. Distance specifies the distance
    to travel for each forward command. Angle specifies the
    angle (in degrees) for each right or left command. The list   
    of turtle supported turtle commands is:
    F : forward
    - : turn right
    + : turn left
    [ : save the turtle's heading and position
    ] : restore the turtle's heading and position
    """
    temp_color = t.pencolor() 
    stack = []
    for c in dstring:
        if c == 'F':
            t.fd(distance)
        elif c == 'c':
            chance = r.randint(0, 10)
            if chance < 5:
                t.color('violetred', 'violetred')
            else:
                t.color('navyblue', 'navyblue')
            t.begin_fill()
            t.circle(distance/4)
            t.end_fill()
            t.color(temp_color)
        elif c == '-':
            t.right(angle)
        elif c == '+':
            t.left(angle)
        elif c == '[':
            stack.append(t.pos())
            stack.append(t.heading())
        elif c == ']':
            t.penup()
            t.setheading(stack.pop())
            t.goto(stack.pop())
            t.pendown()
    t.update()


def hold():
    '''Holds the screen open until user clicks or presses 'q' 
       key'''

    t.hideturtle()
    t.update()
    t.onkey(t.bye, 'q')
    t.listen()
    t.exitonclick()		


