'''Veer Khosla
CS151 A
Project 7
grid23.py'''

import sys
import turtle as t
import lsystem23 as ls
import turtle_interpreter23 as it
import random as r


def grid(lstr, x, y, scale, angle):
    '''goes to specified coordinates and draws l-system with given parameters'''
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()

    it.drawString(lstr, scale, angle)
    return



def main():
    '''creates screen and draws each tree by calling grid function'''
    screen = t.Screen()
    screen.setup(1000, 800)

    lsys = ls.createLsystemFromFile('systemB.txt')
    y = 150
    angles = [22, 46, 60]

    for j in angles:
        x = -400
        for i in range(1, 4):
            lstr = ls.buildString(lsys, i) 
            grid(lstr, x, y, 16-i*3, j)
            x += 300

        y -= 200

    it.hold()    


if __name__ == "__main__":
    main()
