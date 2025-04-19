'''Veer Khosla
CS151 A
Final Project
data.py
'''

import turtle as t
import random as r

import secondText as st
import lsystemFINAL
import turtle_interpreterFINAL


t.tracer(False)
	

def goto(x, y, heading):
    '''goes to any requested coordinates and sets any heading'''
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    t.hideturtle()


def screen():
    '''builds turtle window'''
    mainScreen = t.Screen()
    mainScreen.title('Data')
    mainScreen.setup(700, 600)
    mainScreen.bgcolor('aliceblue')


def water():
    '''draws water'''
    goto(-350, -300, 0)
    t.color('cornflowerblue')
    t.begin_fill()
    t.fd(700)
    t.left(90)
    t.fd(300)
    while t.xcor() > -350 and t.ycor() > -300:
        t.left(150)
        t.fd(75)
        t.right(150)
        t.fd(50)
    t.end_fill()
    t.hideturtle()


def moveAndTurn(distance, angle):
    '''moves and turns by specified distance and angle'''
    t.fd(distance)
    t.setheading(angle)
    t.hideturtle()


def sun():
    '''draws sun'''
    goto(-270, 185, 0)
    t.color('khaki')
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.hideturtle()


def iceberg():
    '''draws iceberg'''
    goto(105, -300, 180)
    t.color('lightblue')
    t.begin_fill()
    moveAndTurn(460, 90)
    t.fd(390)
    moveAndTurn(90, -45)
    moveAndTurn(140, 0)
    moveAndTurn(65, -50)
    moveAndTurn(140, -63)
    moveAndTurn(240, -70)
    t.end_fill()


def fire():
    '''draws fire'''
    t.color('red')
    goto(350, -50, 90)
    t.begin_fill()
    moveAndTurn(150, -110)
    while t.xcor() > 50:
        # moveAndTurn(100, 90)
        t.fd(100)
        t.setheading(90)
        t.fd(70)
        t.setheading(-110)
    while t.xcor() > -150:
        t.setheading(110)
        t.fd(100)
        t.setheading(-90)
        t.fd(70)
        t.setheading(-110)
    t.setheading(-90)
    moveAndTurn(220, 0)
    moveAndTurn(513, 90)
    t.fd(200)
    t.end_fill()
    t.hideturtle()


def cloud():
    '''draws cloud'''
    goto(350, -200, 90)
    t.color('lightgrey')
    t.begin_fill()
    moveAndTurn(500, 180)
    moveAndTurn(150, 230)
    moveAndTurn(75, 190)
    moveAndTurn(50, 220)
    moveAndTurn(50, 170)
    moveAndTurn(75, 230)
    moveAndTurn(75, 220)
    moveAndTurn(75, 210)
    moveAndTurn(50, 190)
    moveAndTurn(200, -90)
    moveAndTurn(200, 0)
    t.fd(710)
    t.end_fill()
    t.hideturtle()


def snowflakes():
    '''draws koch snowflake from data.txt'''
    flake = lsystemFINAL.Lsystem('data.txt')
    draw = turtle_interpreterFINAL.TurtleInterpreter()

    for i in range(30):
        t.hideturtle()
        str = flake.buildString(r.randint(2,3))
        draw.setColor('silver')
        t.begin_fill()
        draw.place(r.randint(-50, 300), r.randint(0, 250), 90)
        draw.setWidth(1.5)
        draw.drawString(str, 1, 60)
        t.end_fill()
    for i in range(10):
        str = flake.buildString(r.randint(1,3))
        draw.setColor('silver')
        t.begin_fill()
        draw.place(r.randint(20, 70), r.randint(-100, 100), 90)
        draw.setWidth(1.5)
        draw.drawString(str, 0.5, 60)
        t.end_fill()


def button():
    '''draws a button at top right corner; click to go to next screen'''
    pen = t.Turtle()
    pen.hideturtle()

    pen.penup()
    pen.goto(290, 265)
    pen.pendown()
    pen.hideturtle()
    for i in range(2):
        pen.forward(50)
        pen.left(90)
        pen.forward(30)
        pen.left(90)
    pen.penup()
    pen.goto(300, 270)
    pen.write("Next!", font=("Arial", 12, "normal"))
    pen.hideturtle()

    def btnclick(x, y):
        if 300 < x < 350 and 250 < y < 300:
            print("Going to secondText.py")
            st.main()

    t.onscreenclick(btnclick, 1)
    t.listen()


def exit():
    '''exits function on "q" keypress'''
    t.listen()
    t.onkeypress(t.bye, 'q')


def main():
    '''executes program'''
    t.clear()
    t.resetscreen()
    exit()
    print('Press Right Arrow to go to next scene or \'Q\' to exit.')

    for i in range(20):
        screen()
        cloud()
        button()
        fire()
        iceberg()
        water()
        sun()
        snowflakes()
        t.hideturtle()
    else:
        t.resetscreen()


if __name__ == '__main__':
    main()