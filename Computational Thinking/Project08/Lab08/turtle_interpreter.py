'''Veer Khosla
CS151 A
Lab 8
turtle_interpreter.py'''

import turtle as t
import random as r
import sys

class TurtleInterpreter:

    def __init__(self, dx = 800, dy = 800):
        '''initializer'''
        t.setup(dx, dy)
        # t.tracer(False)


    def drawString(self, dstring, distance, angle ):
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
        colorstack = []
        for c in dstring:
            if c == 'F':
                t.fd(distance)
            elif c == 'l':
                t.pendown()
                t.color('green')
                t.begin_fill()
                t.circle(distance/4)
                t.end_fill()
                t.color(temp_color)
            elif c == 'B':
                t.fd(-distance)
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
            elif c =='<':
                colorstack.append(t.color()[0])
            elif c == '>':
                t.color(colorstack.pop())
            elif c == 'g':
                t.color(0.15, 0.5, 0.2)
            elif c == 'y':
                t.color(0.8, 0.8, 0.3)
            elif c == 'r':
                t.color(0.7, 0.2, 0.3)

        t.update()


    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' 
        key'''

        t.hideturtle()
        t.update()
        t.onkey(t.bye, 'q')
        t.listen()
        t.exitonclick()		


    def place(self, xpos, ypos, angle = None):
        '''the method should pick up the pen, place the turtle at 
        location (xpos, ypos), orient the turtle if the angle argument is not
        None, and then put down the pen. '''

        t.penup()
        t.goto(xpos, ypos)
        if angle != None:
            t.setheading(angle)
        t.pendown()

    
    def orient(self, angle):
        '''the method should use the turtle's setheading function to set 
        turtle's heading to the given angle.'''

        t.setheading(angle)


    def goto(self, xpos, ypos):
        '''the method should pick up the turtle, send the turtle 
        to (xpos, ypos), and then put the pen down.'''

        t.penup()
        t.goto(xpos, ypos)
        t.pendown()


    def setColor(self, c):
        '''set turtle's color'''

        t.color(c)

    
    def setWidth(self, w):
        '''set turtle's width'''

        t.width(w)