'''Veer Khosla
CS151A
2/16/2022
Lab 3'''

import turtle as t
import random as r
import sys

t.speed(100)

def goto(x, y): 
    '''this function moves turtle to any location'''
    t.up()
    t.goto(x, y)
    t.down()


def rectangle(x, y, width, height, fillColor, edgeColor = 'black', fill = False, penWidth = 1):
    '''Draws a rectangle at coordinates (x, y) of given width and height, edge color, fill color, and pen size'''
    goto(x, y)

    t.pencolor('black')

    if fill == True:
        t.pensize(2)
        t.begin_fill()
        t.color(edgeColor, fillColor)

        for i in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)    

        t.end_fill()

    else:
        for i in range(2):
            t.pensize(penWidth)
            t.color('black', 'black')

            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)

    t.pencolor('black')
    t.pensize(1)


def main():
    '''this function generates a given number rectangles of random color, size, and location'''

    numRect = int(sys.argv[1])

    for i in range(numRect):

        rgb1 = r.random()
        rgb2 = r.random()
        rgb3 = r.random()

        fillColor = (rgb1, rgb2, rgb3)

        if i <= 80:
            rectangle(r.randint(-500, 500), r.randint(-500, 500), r.randint(50, 150), r.randint(50, 150), fillColor, 'black', True)

        else:
            rectangle(r.randint(-500, 500), r.randint(-500, 500), r.randint(50, 150), r.randint(50, 150), fillColor, 'black', False, 2)


# rectangle(-350, -300, 50, 500, 'blue', fill=True)
# rectangle(0, 0, 100, 100, 'black', fill=False)
# rectangle(200, -300, 200, 100, 'black', fill=True)

t.tracer(False)

if __name__ == '__main__':
  main()


t.exitonclick()