'''Veer Khosla
CS151 A
Spring 2023
shapeslib.py
2/9/2023
This file stores functions for Project 2, which are used in file main.py'''

import math as m
import turtle as t
import random as r


def goto(x, y): 
    '''this function moves turtle to any location'''
    print('goto(): going to', x, y)
    print('goto(): before move, turtle at', t.position())
    print('goto(): after move, turtle now at', t.position())
    t.up()
    t.goto(x, y)
    
    t.down()


def block(x, y, width, height):
    '''Draws a block at (x, y) of given width and height'''
    goto(x, y)

    print('block(): drawing block of size', width, height)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)


def bunchOfBlocks(x, y, scale):
    '''This function draws a bunch of blocks relative to a central location'''
    print('bunchOfBlocks(): drawing blocks at location', x, y)

    block(x, y, scale*4, scale*8)
    block(x+1*scale, y+8*scale, 2*scale, 4*scale)
    block(x+1.5*scale, y+12*scale, 1*scale, 2*scale)


def starSun(x, y, length):
    '''Draws 10-sided orange star'''

    goto(x, y)
    t.setheading(0)

    t.begin_fill()
    t.color('orange')
    for i in range(10):
        for i in range(5):
            
            t.forward(length*1.3)
            t.right(144)

        t.right(36)
    t.end_fill()
    return length


def circleSun(x, y, radius):
    '''Draws a dark orange circle at (x, y) with given radius'''

    goto(x, y - radius)
    t.setheading(0)

    t.begin_fill()
    t.color('darkorange')
    t.circle(radius)
    t.end_fill()


def sun(x, y, radius):
    '''this function puts the circleSun function image on top of the starSun function image, to create a more complete and detailed sun'''
    starSun(x, y, radius)
    circleSun(x, y, radius)
    

def grassOrWater(x, y, sideLength1, sideLength2, color):
    '''this function draws triangles with any given side lengths and color, at any given coordinates'''

    t.penup()
    t.goto(x, y)
    
    if color == 'green':
        t.setheading(0)
    t.pendown()

    hypo = m.sqrt(sideLength1**2 + sideLength2**2)
    angleA = m.degrees(m.asin(sideLength2 / hypo))
    angleB = m.degrees(m.asin(sideLength1 / hypo))

    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()

    t.forward(sideLength1)
    t.left(180 - angleA)
    t.forward(hypo)
    t.left(180 - angleB)
    t.forward(sideLength2)


    t.end_fill()
    t.penup()


def rectangle(x, y, scale, color):
    '''this function makes a rectangle of any color at any given coordinates'''
    goto(x, y)
    if color == 'green':
        t.setheading(0)

    t.pencolor(color)
    t.begin_fill()
    t.fillcolor(color)

    for i in range(2):
        t.forward(200*scale)
        t.left(90)
        t.forward(400*scale)
        t.left(90)

    t.end_fill()


def skyRectangle(x, y, color):
    '''this function makes a rectangle of any color at any given coordinates for the sky.'''
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.setheading(0)

    t.pencolor(color)
    t.begin_fill()
    t.fillcolor(color)

    for i in range(2):
        t.forward(900)
        t.left(90)
        t.forward(25)
        t.left(90)

    t.end_fill()


def skyBlueRectangle(x, y):
    '''this function makes a rectangle that is large and blue at any given coordinates'''
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.pencolor('dodgerblue')
    t.begin_fill()
    t.fillcolor('dodgerblue')

    for i in range(2):
        t.forward(900)
        t.left(90)
        t.forward(200)
        t.left(90)

    t.end_fill()


def sky():
    '''this function draws the sky with different coordinates and color arguments from the skyRectangle function'''
    skyRectangle(-450, 50, 'darkorange1')
    skyRectangle(-450, 75, 'gold')
    skyRectangle(-450, 100, 'lightgoldenrod1')
    skyRectangle(-450, 125, 'khaki1')
    skyRectangle(-450, 150, 'paleturquoise1')
    skyRectangle(-450, 175, 'skyblue1')
    skyRectangle(-450, 200, 'deepskyblue')
    skyBlueRectangle(-450, 225)


# FUNCTIONS FOR EXTENSION:
def moon(x, y, radius):
    '''Draws a white circle at any given coordinates with any given radius'''

    goto(x, y - radius)
    t.setheading(0)

    t.begin_fill()
    t.color('white')
    t.circle(radius)
    t.end_fill()


def moonRandom():
    '''This function takes my moon function and inputs random coordinates to display the moon anywhere in the sky'''
    moon(r.randint(-350, 350), r.randint(115, 250), 50)
    t.hideturtle()


def sunRandom():
    '''This function takes my sun function and inputs random coordinates to display the sun anywhere in the sky'''
    sun(r.randint(-350, 350), r.randint(115, 250), 50)
    t.hideturtle()


def stars():
    '''this function creates 30 tiny white circles as stars in random locations'''
    for i in range(30):
        t.penup()
        t.goto(r.randint(-350, 350), r.randint(150,300))
        t.pendown()

        t.begin_fill()
        t.color('white')
        t.circle(1)
        t.end_fill()


def nightSky():
    '''This function creates a black, night sky'''
    t.penup()
    t.goto(-450, 50)
    t.pendown()
    t.setheading(0)

    t.pencolor('black')
    t.begin_fill()
    t.fillcolor('black')

    for i in range(4):
        t.forward(900)
        t.left(90)

    t.end_fill()