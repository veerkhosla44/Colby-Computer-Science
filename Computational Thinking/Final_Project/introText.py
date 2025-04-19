'''Veer Khosla
CS151 A
Final Project
introText.py
'''

import turtle as t
import data

SCREEN = t.Screen()
SCREEN.setup(700, 600)    


def button():
    '''draws a button at top right corner; click to go to next screen'''
    pen = t.Turtle()
    pen.hideturtle()

    pen.penup()
    pen.goto(290, 265)
    pen.pendown()
    pen.hideturtle()
    for i in range(2):
        pen.forward(50)
        pen.left(90)
        pen.forward(30)
        pen.left(90)

    pen.penup()
    pen.goto(300, 270)
    pen.write("Next!", font=("Arial", 12, "normal"))
    pen.hideturtle()

    def btnclick(x, y):
        if 300 < x < 350 and 250 < y < 300:
            print("Going to data.py")
            data.main()

    t.onscreenclick(btnclick, 1)
    t.listen()


def exit():
    '''exits function on "q" keypress'''
    t.listen()
    t.onkeypress(t.bye, 'q')
    t.listen()


def text():
    '''writes text on screen'''
    t.penup()
    t.goto(-330, 0)
    t.pendown()
    t.write('The ice caps are melting as a result of human pollution. Icebergs are melting, water levels are increasing, and \n  our atmosphere is becoming more and more polluted \n          with ash and smog. Click "Next" to see.', font = ("Arial", 20, "normal"))


def main():
    '''draws scene'''
    t.clear()
    while True:
        button()
        text()
        exit()


if __name__ == "__main__":
    main()