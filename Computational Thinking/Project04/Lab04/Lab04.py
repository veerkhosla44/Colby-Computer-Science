'''Veer Khosla
CS151 A
2/23/2023
Lab04.py'''

import turtle as t
import random as r

def make_screen(width, height, title, color='black'):
    '''Makes a 'Screen' object: the window in each turtles can draw shapes

    Parameters:
    -----------
    width: int.
        The width of the window/screen in pixels.
    height: int.
        the height of the window/screen in pixels.
    title: str.
        the name of the pop-up window. Appears at the center of top of the window.
    color: str.
        Color string ame. This is the background color of the screen.

    Returns
    -------
        The 'Screen' object that you create
    '''

    screen = t.Screen()

    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor(color)

    return screen


def make_turtle(shape='turtle', penColor='white'):
    '''Makes a 'Turtle' object
    
    Parameters
    ----------
    shape: str.
        options: 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
    penColor: str.
        Color string name that is to be the pen color of this turtle.

    Returns
    -------
    The 'Turtle' object that is created
    '''

    turtle1 = t.Turtle()

    turtle1.shape(shape)
    turtle1.pencolor(penColor)
    turtle1.penup()
    
    return turtle1


def reset_turtle(turt, screen_width, screen_height):
    '''resets the turtle'''

    turt.goto(r.randint(-screen_width/2 + 10 , screen_width/2 - 10), screen_height/2 - 10)
    turt.setheading(270)
    turt.color( (r.random(), r.random(), r.random()) , (r.random(), r.random(), r.random()) )

    return turt


def move_and_stamp(turt, distance):
    '''stamps turtle down where it is and moves forward by specified distance'''
    turt.stamp()
    turt.fd(distance + r.randint(0, 10))
            
    return turt


def writeNumStrides(turt, numStrides):
    '''writes the number of total strides, or the total number of times turtles reset, at the top of the screen'''
    turt.clear()
    turt.penup()
    turt.write(numStrides, font=('Arial', 30, 'normal'))
    turt.hideturtle()

    return turt


def main():
    '''Makes screen, 3 unique turtles, and counter all as objects. Iterates 1000x to move turtles. resets turtle position when one hits the bottom of the screen'''
    t.speed(0)
    screen = make_screen(500, 500, 'Turtle Tracks')
    
    x = screen.window_width()
    y = screen.window_height()

    turt1 = make_turtle('arrow', 'white')
    turt2 = make_turtle('turtle', 'blue')
    turt3 = make_turtle('classic', 'orange')

    reset_turtle(turt1, x, y)
    reset_turtle(turt2, x, y)
    reset_turtle(turt3, x, y)

    numStrides = 0
    counter = make_turtle('turtle', 'white')
    counter.penup()
    counter.goto(0, y/2 - 40)
    writeNumStrides(counter, numStrides)

    for i in range(1000):
        move_and_stamp(turt1, 40)
        move_and_stamp(turt2, 30)
        move_and_stamp(turt3, 20)

        if turt1.ycor() <= -y/2:
            reset_turtle(turt1, x, y)
            numStrides += 1
            writeNumStrides(counter, numStrides)
        elif turt2.ycor() <= -y/2:
            reset_turtle(turt2, x, y)
            numStrides += 1
            writeNumStrides(counter, numStrides)
        elif turt3.ycor() <= -y/2:
            reset_turtle(turt3, x, y)
            numStrides += 1
            writeNumStrides(counter, numStrides)
    

if __name__ == '__main__':
    main()

t.exitonclick()