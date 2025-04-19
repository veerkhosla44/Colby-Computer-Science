'''turtle_interpreter22.py
Converts L-System string into turtle commands for Lab 8/9
CS151 Visual Media, Fall 2022
'''

import turtle


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
    stack = []
    for char in dstring:
        if char == 'F':
            turtle.forward(distance)
        elif char == '-':
            turtle.right(angle)
        elif char == '+':
            turtle.left(angle)
        elif char == '[':
            stack.append(turtle.position())
            stack.append(turtle.heading())
        elif char == ']':
            turtle.penup()
            turtle.setheading(stack.pop())
            turtle.goto(stack.pop())
            turtle.pendown()
    turtle.update()


def hold():
    '''Holds the screen open until user clicks or presses 'q' 
       key'''

    # Hide the turtle cursor and update the screen
    turtle.hideturtle()
    turtle.update()

    # Close the window when users presses the 'q' key
    turtle.onkey(turtle.bye, 'q')

    # Listen for the q button press event
    turtle.listen()

    # Have the turtle listen for a click
    turtle.exitonclick()