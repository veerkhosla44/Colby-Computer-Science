'''Veer Khosla
CS151 A
Project 7
abstract23.py'''


import sys
import turtle as t
import lsystem23 as ls
import turtle_interpreter23 as it
import random as r


def circle(lstr, x, y, scale, angle ):
    '''makes abstract circle'''
    color = r.random(), r.random(), r.random()

    # oldheading = t.heading()

    t.up()
    t.goto(x, y)
    t.down()
    t.right(270)
    t.color(color)
    t.width(2)
    it.drawString(lstr, scale*0.75, angle)


def tree(lstr, x, y, scale, angle, heading):
    '''makes geometic pattern'''
    color = r.random(), r.random(), r.random()

    t.up()
    t.goto(x, y)
    t.setheading(heading)
    t.down()
    t.color(color)
    t.width(2)

    # t.forward(distance)
    it.drawString(lstr, scale*0.75, angle)


def geometry(lstr, x, y, scale, angle ):
    '''makes tree'''
    color = r.random(), r.random(), r.random()

    heading = t.heading()

    for i in range(24):
        t.up()
        t.goto(x, y)
        t.setheading(heading)
        t.down()
        t.color(color)

        heading += 15

        it.drawString(lstr, scale*0.75, angle)


# def testCircle(lstr1):
#     '''draws circle at 3 different locations and sizes'''
#     circle(lstr1, -200, 200, 10, 10)
#     circle(lstr1, -200, 0, 5, 10)
#     circle(lstr1, -100, -200, 3, 10)


# def testTree(lstr2):
#     '''draws tree at 3 different locations and sizes'''
#     tree(lstr2, 200, 200, 10, 20, 20)
#     tree(lstr2, 100, 0, 10, 25, 20)
#     tree(lstr2, 100, -200, 15, 10, 20)


# def testGeometry(lstr3):
#     '''draws geometric pattern at 3 different locations and sizes'''
#     geometry(lstr3, 0, 200, 30, 90)
#     geometry(lstr3, 0, 0, 20, 90)
#     geometry(lstr3, 0, -200, 10, 90)


def main():
    screen_width = t.window_width()
    screen_height = t.window_height()

    '''calls l-systems from respective txt files and calls functions'''
    lsys = ls.createLsystemFromFile('abstract1.txt')
    lsys2 = ls.createLsystemFromFile('abstract2.txt')
    lsys3 = ls.createLsystemFromFile('abstract3.txt')

    lstr1 = ls.buildString(lsys, 3)
    lstr2 = ls.buildString(lsys2, 3)
    lstr3 = ls.buildString(lsys3, 3)

    t.tracer(False)

    geometry(lstr3, 0, screen_height / 2, 45, 5)
    geometry(lstr3, screen_width / 2, 10, 45, 5)
    geometry(lstr3, 0, -screen_height / 2, 45, 5)
    geometry(lstr3, -screen_width / 2, 10 / 2, 45, 5)


    circle(lstr1, -150, -20, 20, 10)
    geometry(lstr3, 0, 10, 60, 45)

    tree(lstr2, -screen_width / 2, -screen_height / 2, 10, 15, 60)
    tree(lstr2, -screen_width / 2, screen_height / 2, 10, 15, 300)
    tree(lstr2, screen_width / 2, -screen_height / 2, 10, 15, 120)
    tree(lstr2, screen_width / 2, screen_height / 2, 10, 15, 240)

    circle(lstr1, -140, -175, 30, 10)

    geometry(lstr3, 0, screen_height / 2, 45, 20)
    geometry(lstr3, screen_width / 2, 10, 45, 20)
    geometry(lstr3, 0, -screen_height / 2, 45, 20)
    geometry(lstr3, -screen_width / 2, 10 / 2, 45, 20)

 
    # testCircle(lstr1)
    # testTree(lstr2)
    # testGeometry(lstr3)
    
    # wait
    it.hold()


if __name__ == "__main__":
    main()

