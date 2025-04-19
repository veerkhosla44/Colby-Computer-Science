'''Veer Khosla
CS151 A
Final Project
realismFINAL.py
'''

import graphicsPlus as gr
import complex_shapes as cs
import random as r
import sys

import intro
import outro

def draw (shapes, win):
    '''A for loop that draws each item in the given list of shapes'''
    for item in shapes:
        item.draw(win)


def water(win):
    '''draws the water'''
    Water = gr.Rectangle(gr.Point(0, 200), gr.Point(1000, 700))
    Water.setFill(gr.color_rgb(0,105,148))
    Water.setOutline(gr.color_rgb(0,105,148))
    Water.draw(win)
    

def skyDay(win):
    '''makes rectangles 1000x1 and gradually changes the color as the y value increases in the while loop'''
    y = 0
    r1 = 98
    g1 = 151
    b1 = 159

    r2 = 131
    g2 = 165
    b2 = 149

    while y < 200:
        r = int(r1 + (r2 - r1) * y / 200)
        g = int(g1 + (g2 - g1) * y / 200)
        b = int(b1 + (b2 - b1) * y / 200)
        Sky = gr.Rectangle(gr.Point(0, y), gr.Point(1000, y+1))
        Sky.setFill(gr.color_rgb(r, g, b))
        Sky.setOutline(gr.color_rgb(r, g, b))
        Sky.draw(win)

        y += 1


def cratesAndBarrels(win):
    '''draws crates and barrels from complex_shapes.py at various locations and sizes'''
    Crate1 = cs.crate_init(200, 500, 1.7)
    Crate2 = cs.crate_init(650, 350, 0.8)
    Crate3 = cs.crate_init(800, 250, 0.3)

    Barrel1 = cs.barrel_init(850, 300, 0.9)
    Barrel2 = cs.barrel_init(300, 275, 0.3)
    Barrel3 = cs.barrel_init(100, 400, 1.3)

    draw(Crate1, win)
    draw(Crate2, win)
    draw(Crate3, win)

    draw(Barrel1, win)
    draw(Barrel2, win)
    draw(Barrel3, win)


def litter(win, litterShapes):
    '''draws bottle objects at various coordinates and sizes '''
    radius = 5
    x = 50
    for i in range(10):
        bottle = gr.Circle(gr.Point(x, 600), radius)
        bottle.setFill('white')
        bottle.setOutline('white')
        bottle.draw(win)
        litterShapes.append(bottle)

        radius += 3
        x += 100


def bearStuff(x, y, win):
    '''creates and draws bear related images and objects'''
    Iceberg = cs.iceberg_init(400, 300, 1)
    draw(Iceberg, win)
    Bear = gr.Image(gr.Point(x, y), 'PolarBear.gif')
    Bear.draw(win)


def button(win):
    '''draws a button at top right corner; click to go to next screen'''
    rect = gr.Rectangle(gr.Point(949, 0), gr.Point(999, 30))
    rect.draw(win)
    label = gr.Text(gr.Point(974, 15), "Next!")
    label.draw(win)

    while True:
        click = win.getMouse()

        if 949 < click.getX() < 999 and 0 < click.getY() < 30:
            print("Going to outro.py")
            outro.outro()
            win.close()
            break


def main():
    '''draws full scene'''
    win = gr.GraphWin('Climate Change Bear', 1000, 700)
    litterShapes = []

    water(win)
    skyDay(win)
    cratesAndBarrels(win)
    bearStuff(500, 215, win)

    litter(win, litterShapes)


    for i in range(5):
        for shape in litterShapes:
            shape.move(0,2)
            gr.time.sleep(0.03)
        for shape in litterShapes:
            shape.move(0, -4)
            gr.time.sleep(0.03)
        for shape in litterShapes:
            shape.move(0, 2)
            gr.time.sleep(0.03)


        if win.checkMouse() is not None:
            win.getMouse()
            win.close()
            break

    for shape in litterShapes:
        shape.undraw()

    litter(win, litterShapes)
    button(win)
    win.getMouse()
    win.close()
    intro.setFalse()


if __name__ == "__main__":
    main()
