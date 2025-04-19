'''Veer Khosla
CS151 A
Spring 2023
Lab2.py
2/9/2023
This file walks goes through the instructions of Lab2.'''

import random as r
import turtle as t

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

    

print('running main code')

for i in range(10):
    bunchOfBlocks(r.random()*600 - 300, r.random()*600 - 300, r.random()*10 + 0.5)

input('Press enter to continue')