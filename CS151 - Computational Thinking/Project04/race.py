'''Veer Khosla
CS151 A
3/8/2023
Project 04
race.py'''

import turtle as t
import random as r
import object_shapelib as osl


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


def writeNumStrides1(turt):
    '''counts number of laps completed by racer1 (turtle)'''

    turt.clear()
    turt.penup()
    turt.write('Turtle: ' + str(turt.numStrides), font=('Arial', 30, 'normal'))
    turt.hideturtle()

    return turt


def writeNumStrides2(turt):
    '''counts number of laps completed by racer2 (Pointer)'''
    turt.clear()
    turt.penup()
    turt.write('Pointer: ' + str(turt.numStrides2), font=('Arial', 30, 'normal'))
    turt.hideturtle()

    return turt


numStrides = 0
numStrides2 = 0


def move_turtles(turt1, turt2, speeds, counter1, counter2):
    '''this function moves turtles 1 and 2 at speeds input with arguments, and keeps track of how many laps each turtle completes'''
    speed1, speed2 = speeds

    turt1.speed(speed1 + r.randint(-1,1))
    turt2.speed(speed2 + r.randint(-1,1))

    counter1.penup()
    counter1.goto(-400, 250)
    writeNumStrides1(counter1)

    counter2.penup()
    counter2.goto(250, 250)
    writeNumStrides2(counter2)



    while turt1.xcor() <= 150: #FIRST STRAIGHT
        turt1.forward(speed1 + r.randint(-1,1))
        turt2.forward(speed2 + r.randint(-1,1))
    
    while turt1.ycor() <= 162: #FIRST TURN
        turt1.circle(63, 9)
        if turt2.xcor() <= 150:
            turt2.forward(speed2 + r.randint(-1,1))
        else:
            turt2.circle(87, 9)
    else:
            turt1.setheading(180)
            turt1.forward(speed1 + r.randint(-1,1))
            if turt2.xcor() <= 150:
                turt2.forward(speed2 + r.randint(-1,1))
            else:
                if turt2.ycor() < 185:
                    turt2.circle(87, 9)
                else:
                    turt2.setheading(180)
                    turt2.forward(speed2 + r.randint(-1,1))

    while turt1.xcor() >= -150: #SECOND STRAIGHT
        turt1.forward(speed1 + r.randint(-1,1))
        if turt2.ycor() < 185:
            turt2.circle(87, 9)
        else:
            turt2.setheading(180)
            if turt2.xcor() >= -150:
                turt2.forward(speed2 + r.randint(-1,1))
    else:
        while turt1.ycor() >= 37: #SECOND TURN
            turt1.circle(63, 9)
            if turt2.xcor() >= -150:
                turt2.forward(speed2 + r.randint(-1,1))
            else:
                turt2.circle(87, 9)
        else:
            turt1.setheading(0)
            turt1.forward(speed1 + r.randint(-1,1))
            if turt2.xcor() >= -150:
                turt2.forward(speed2 + r.randint(-1,1))
            else:
                if turt2.ycor() > 13:
                    turt2.circle(87, 9)
                else:
                    turt2.setheading(0)
                    turt2.forward(speed2 + r.randint(-1,1))
    
    while turt1.xcor() < 0: #FINISHING SEGMENT
        turt1.forward(speed1 + r.randint(-1,1))
        if turt2.ycor() > 13:
            turt2.circle(87, 9)
        else:
            turt2.setheading(0)
            if turt2.xcor() < 0:
                turt2.forward(speed2 + r.randint(-1,1))

    counter1.numStrides += 1
    writeNumStrides1(counter1)
    print(counter1.numStrides)



    while turt2.xcor() < 0:
        turt1.forward(speed1 + r.randint(-1,1))
        turt2.forward(speed2 + r.randint(-1,1))

    counter2.numStrides2 += 1
    writeNumStrides2(counter2)
    print(counter2.numStrides2)


def make_spectators_turtles(x, y, iter):
    '''this function makes spectator objects a specified number of times at coordiates, facing towards the track'''
    t.speed(0)

    for i in range(iter):
        turtle = make_turtle('turtle')
        turtle.goto(x, y)
        turtle.setheading(270)
        x += 30


def make_spectators_pointers(x, y, iter):
    '''this function makes spectators using move_and_stamp_specs'''
    t.speed(0)

    for i in range(iter):
        pointer = make_turtle('classic')
        pointer.goto(x, y)
        pointer.setheading(270)
        x += 30


def main():
    '''draws race track and background, creates racing turtles and counters. moves turtles around track 1000x'''

    osl.draw_race_scene(1000, 800, 'Race Track', 'green')

    racer1 = make_turtle()
    racer2 = make_turtle('classic')

    racer1.goto(0,37)
    racer2.goto(0,13)

    counter1 = make_turtle('turtle', 'yellow')
    counter1.numStrides = 0

    counter2 = make_turtle('turtle', 'yellow')
    counter2.numStrides2 = 0

    t.speed(0)

    make_spectators_turtles(-185, 385, 6)
    make_spectators_pointers(15, 377.5, 6)

    make_spectators_turtles(-135, 335, 5)
    make_spectators_pointers(15, 327.5, 5)

    make_spectators_turtles(-85, 285, 3)
    make_spectators_pointers(15, 277.5, 3)

    t.hideturtle()


    for i in range(1000):
        move_turtles(racer1, racer2, (5, 4.9), counter1, counter2)


if __name__ == '__main__':
    main()
    t.exitonclick()
