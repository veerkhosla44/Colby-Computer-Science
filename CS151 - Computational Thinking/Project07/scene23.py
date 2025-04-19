'''Veer Khosla
CS151 A
Project 7
scene23.py'''

import turtle as t
import random as r
import lsystem23 as ls
import turtle_interpreter23 as it


t.tracer(False)
# t.speed(0)


def goto(x, y):
    '''goes to any specified coordinates'''
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()


def sky():
    '''draws sky with gradient colors'''
    y = 350

    #colors
    r1 = 237
    g1 = 172
    b1 = 114

    r2 = 97
    g2 = 108
    b2 = 170

    while y > 100:
        r = int(r1 + (r2 - r1) * (y - 100) / 250)
        g = int(g1 + (g2 - g1) * (y - 100) / 250)
        b = int(b1 + (b2 - b1) * (y - 100) / 250)

        goto(-400, y)
        t.pencolor(r, g, b)
        t.forward(800)

        y -= 1


def house():
    '''draws rectangle and triangle for house body and roof of grey color'''
    goto(-400, -115)
    t.pencolor('black')
    t.begin_fill()
    for i in range(2):
        t.forward(800)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.fillcolor('grey')
    t.end_fill()

    goto(-400, 135)
    t.begin_fill()
    t.forward(800)
    t.left(160)
    t.fd(435)
    t.left(41)
    t.fd(435)
    t.fillcolor('dimgrey')
    t.end_fill()


def pillars(x, y):
    '''draws pillars and triangle in front of house of white color'''
    goto(x, y)
    t.color('whitesmoke', 'whitesmoke')
    t.begin_fill()
    for i in range(2):
        t.fd(50)
        t.left(90)
        t.fd(150)
        t.left(90)
    t.end_fill()
    t.hideturtle()

    goto(-150, 35)
    t.begin_fill()
    t.forward(300)
    t.left(150)
    t.fd(175)
    t.left(60)
    t.fd(175)
    t.end_fill()
    

def ground():
    '''draws the ground of green grass'''
    goto(-400, -350)
    t.pencolor('darkgreen')
    t.begin_fill()
    for i in range(2):
        t.forward(800)
        t.left(90)
        t.forward(235)
        t.left(90)

    t.fillcolor('darkgreen')
    t.end_fill()


def path():
    '''draws the trapezoidal path of grey color to give the scene a 3D feel'''
    goto(-130, -350)
    t.setheading(70)
    t.pencolor('darkgrey')
    t.begin_fill()
    t.forward(250)
    t.right(70)
    t.forward(100)
    t.right(70)
    t.forward(250)
    t.right(110)
    t.forward(275)
    t.fillcolor('darkgrey')
    t.end_fill()
    t.penup()


def windows(x, y, r):
    '''draws circular windows with panes going across both directions at any specified coordinates. Movable and scalable with chosen radius.'''
    goto(x, y)
    t.color('black', 'gainsboro')
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    t.pensize(3)
    goto(x, y)
    t.setheading(90)
    t.forward(r*2)
    goto(x - r, y + r)
    t.forward(r*2)
    t.pensize(1)


def pots(x, y, scale):
    '''draws gardening pots at any location and scale of red color. '''

    goto(x, y)
    t.color('firebrick', 'firebrick')
    t.begin_fill()

    t.forward(30 * scale)
    t.left(80)
    t.forward(50 * scale)
    t.left(100)
    t.forward(50 * scale)
    t.left(102)
    t.forward(50 * scale)
    t.end_fill()
    t.hideturtle()


def door():
    '''draws door with door knob'''
    goto(-25, -115)
    t.color('brown', 'brown')
    t.begin_fill()
    for i in range(2):
        t.fd(60)
        t.left(90)
        t.fd(100)
        t.left(90)
    t.end_fill()

    goto(25, -75)
    t.color('white', 'white')
    t.begin_fill()
    t.circle(5)
    t.end_fill()


def lsystem(lstr, x, y, scale, angle, color):
    '''sets up lsystem in this py file'''
    heading = t.heading()
    goto(x, y)
    t.setheading(90)
    t.color(color)
    heading += 15
    it.drawString(lstr, scale*0.75, angle)


def scene():
    '''draws full scene. Creates screen object and imports txt files for lsystems. then calls all functions to create composite scene.'''
    screen = t.Screen()
    screen.setup(800, 700)
    screen.colormode(255)

    lsys = ls.createLsystemFromFile('scenePlants.txt')
    lsys2 = ls.createLsystemFromFile('sceneTree.txt')
    lstr1 = ls.buildString(lsys, 2)
    lstr2 = ls.buildString(lsys, 3)
    lstr3 = ls.buildString(lsys2, 3)

    sky()
    house()
    ground()
    path()
    pillars(-150, -115)
    pillars(100, -115)
    windows(0, 150, 50)
    windows(250, -50,75)
    windows(-250, -50, 75)
    door()
    lsystem(lstr1, -150, -310, 10, 10, 'lightgreen')
    lsystem(lstr1, 150, -310, 10, 10, 'green')
    lsystem(lstr2, -110, -180, 7, 10, 'green')
    lsystem(lstr2, 110, -180, 7, 10, 'lightgreen')
    pots(-165, -350, 1)
    pots(140, -350, 1)
    pots(-120, -200, 0.6)
    pots(100, -200, 0.6)
    lsystem(lstr3, 350, -300, 10, 15, 'burlywood')


def main():
    '''calls scene function and exits on click'''
    scene()
    t.exitonclick()


if __name__ == '__main__':
    main()