'''Veer Khosla
3/30/2023
CS151 A
Project 6
realism.py
'''

import graphicsPlus as gr
import complex_shapes as cs
import random as r
import sys

def draw (shapes, win):
    '''A for loop that draws each item in the given list of shapes'''
    for item in shapes:
        item.draw(win)


def iceberg(win):
    '''imports iceberg from complex_shapes.py'''
    Iceberg = cs.iceberg_init(400, 300, 1)
    draw(Iceberg, win)


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


def skyNight(win):
    '''makes black rectangle with white circles as stars'''
    Sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 200))
    Sky.setFill('black')
    Sky.setOutline('black')
    Sky.draw(win)

    for i in range(100):
        stars = gr.Circle(gr.Point(r.randint(0, 1000), r.randint(0, 200)), 2)
        stars.setFill('white')
        stars.draw(win)



def litter(win, litterShapes):
    '''draws bottle objects at various coordinates and sizes '''
    for i in range(30):
        bottle = gr.Circle(gr.Point(r.randint(0, 1000), r.randint(220, 300)), 1.5)
        bottle.setFill('white')
        bottle.setOutline('white')
        bottle.draw(win)
        litterShapes.append(bottle)
    for i in range(30):
        bottle = gr.Circle(gr.Point(r.randint(0, 300), r.randint(250, 500)), 3)
        bottle.setFill('white')
        bottle.setOutline('white')
        bottle.draw(win)
        litterShapes.append(bottle)
    for i in range(30):
        bottle = gr.Circle(gr.Point(r.randint(700, 1000), r.randint(250, 500)), 3)
        bottle.setFill('white')
        bottle.setOutline('white')
        bottle.draw(win)
        litterShapes.append(bottle)
    for i in range(20):
        bottle = gr.Circle(gr.Point(r.randint(0, 300), r.randint(500, 700)), 4)
        bottle.setFill('white')
        bottle.setOutline('white')
        bottle.draw(win)
        litterShapes.append(bottle)
    for i in range(20):
        bottle = gr.Circle(gr.Point(r.randint(700, 1000), r.randint(500, 700)), 5)
        bottle.setFill('white')
        bottle.setOutline('white')
        bottle.draw(win)
        litterShapes.append(bottle)
    for i in range(15):
        bottle = gr.Circle(gr.Point(r.randint(300, 700), r.randint(400, 700)), 4)
        bottle.setFill('white')
        bottle.setOutline('white')
        bottle.draw(win)
        litterShapes.append(bottle)


def cratesAndBarrels(win):
    '''draws crates and barrels from complex_shapes.py at various locations and sizes'''
    Crate1 = cs.crate_init(300, 600, 1.7)
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


def bear(x, y, win):
    '''imports bear from original image into scene'''
    Bear = gr.Image(gr.Point(x, y), 'PolarBear.gif')
    Bear.draw(win)


def main():
    '''draws full scene'''
    win = gr.GraphWin('Climate Change Bear', 1000, 700)
    litterShapes = []

    print('please enter \'day\' or \'night\'')
    if sys.argv[1] == 'day':
        water(win)
        skyDay(win)

        litter(win, litterShapes)
        cratesAndBarrels(win)
        iceberg(win)
        bear(500, 215, win)

        for i in range(10000):
            for shape in litterShapes:
                shape.move(r.randint(-1, 1), r.randint(-1, 1))
            gr.time.sleep(0.05)
            if win.checkMouse() is not None:
                win.getMouse()
                win.close()             
                break

        for shape in litterShapes:
            shape.undraw()

        win.getMouse()
        win.close()

    elif sys.argv[1] == 'night':
        water(win)
        skyNight(win)

        litter(win, litterShapes)
        cratesAndBarrels(win)
        iceberg(win)
        bear(500, 215, win)

        for i in range(10000):
            for shape in litterShapes:
                shape.move(r.randint(-1, 1), r.randint(-1, 1))
            gr.time.sleep(0.05)
            if win.checkMouse() is not None:
                win.getMouse()
                win.close()
                break

        for shape in litterShapes:
            shape.undraw()

        win.getMouse()
        win.close()

    else:
        print('Not a time of day: please enter \'day\' or \'night\'')


if __name__ == "__main__":
    main()
