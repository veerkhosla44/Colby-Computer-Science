'''Veer Khosla
CS151 A
Final Project
outro.py
'''

import graphicsPlus as gr
import complex_shapes as cs
import random as r
import sys



def text(win):
    '''draws text on screen'''
    text = gr.Text(gr.Point(500, 200), "Thank you for taking the time to learn about climate change. \nIn order to make a change, we have to educate others on how to\n  treat the planet and live sustainably. We can work on reducing our \nindividual carbon footprints before working up and \nreducing footprints at much larger scales")
    text.setSize(20)
    text.draw(win)


    text2 = gr.Text(gr.Point(500, 400), "Let's work on saving our planet! \n\nPress 'Close' in the top right at any time to exit.")
    text2.setSize(20)
    text2.draw(win)


def bkgrnd(win):
    '''makes rectangles 1000x1 and gradually changes the color as the y value increases in the while loop'''
    y = 0
    r1 = 98
    g1 = 151
    b1 = 159

    r2 = 131
    g2 = 165
    b2 = 149

    while y <= 700:
        r = int(r1 + (r2 - r1) * y / 700)
        g = int(g1 + (g2 - g1) * y / 700)
        b = int(b1 + (b2 - b1) * y / 700)
        Sky = gr.Rectangle(gr.Point(0, y), gr.Point(1000, y+1))
        Sky.setFill(gr.color_rgb(r, g, b))
        Sky.setOutline(gr.color_rgb(r, g, b))
        Sky.draw(win)

        y += 1


def button(win):
    '''draws a button at top right corner; click to go to close'''
    rect = gr.Rectangle(gr.Point(949, 0), gr.Point(999, 30))
    rect.draw(win)
    label = gr.Text(gr.Point(974, 15), "Close!")
    label.draw(win)


    while True:
        click = win.getMouse()

        if 949 < click.getX() < 999 and 0 < click.getY() < 30:
            print('Terminating Program.')
            win.close()
            break


def main():
    '''creates window and calls functions'''
    win = gr.GraphWin('Outro', 1000, 700)
    bkgrnd(win)
    text(win)
    button(win)


def outro():
    '''calls main'''
    main()


if __name__ == "__main__":
    main()
