'''Veer Khosla
3/30/2023
CS151 A
Lab 6
lab6_collage_animation.py
'''

import graphicsPlus as gr
import time as t
import random as r


def shapeFunc(shapes, win):
    Oval = gr.Oval(gr.Point(100,200), gr.Point(50, 150))
    Oval.draw(win)
    Oval.setFill('blue')
    Oval.setWidth(5)
    Oval.setOutline('yellow')
    shapes.append(Oval)

    Iceberg = gr.Polygon(gr.Point(300, 300), gr.Point(250, 400), gr.Point(350, 430), gr.Point(500, 400), gr.Point(470, 300))
    Iceberg.draw(win)
    Iceberg.setFill(gr.color_rgb(113, 166, 210))
    Iceberg.setWidth(4)
    Iceberg.setOutline(gr.color_rgb(27, 94, 152))
    shapes.append(Iceberg)

    Trash = gr.Polygon(gr.Point(200, 500), gr.Point(250, 500), gr.Point(270, 480), gr.Point(250, 450),gr.Point(225, 470), gr.Point(225, 470))
    Trash.draw(win)
    Trash.setFill('green')
    Trash.setOutline('darkgreen')
    Trash.setWidth(3)
    shapes.append(Trash)


def main():
    shapes = []

    win = gr.GraphWin('Collage', 1000, 700)
    win.setBackground('grey')

    shapeFunc(shapes, win)
    
    for i in range(1000):
        for shape in shapes:
            shape.move(r.randint(-10, 10), r.randint(-10, 10))
            shape.setFill(gr.color_rgb(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
            t.sleep(0.5)
        if win.checkMouse() is not None:
            break

    for shape in shapes:
        shape.undraw()
        shape.draw(win)


    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()