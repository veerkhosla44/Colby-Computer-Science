'''Veer Khosla
CS151 A
Final Project
secondText.py
'''

import turtle as t
import realismFINAL as rl

import data

SCREEN2 = t.Screen()
SCREEN2.setup(700, 600)    


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
            print("Going to realismFINAL.py")
            rl.main()

    t.onscreenclick(btnclick, 1)
    t.listen()


def text():
    '''draws text to screen'''
    t.penup()
    t.goto(-340, 50)
    t.pendown()
    t.write('As seen, there are huge amounts of changes happening \n  in the global environment due to pollution. Additionally, \n  plastic levels are expected to double by 2050, leaving \n               polar animals absolutely devastated. ', font = ("Arial", 20, "normal"))


def exit():
    '''exits function on "q" keypress'''
    t.listen()
    t.onkeypress(t.bye, 'q')
    t.listen()


def main():
    '''draws scene'''
    t.clear()
    t.resetscreen()
    while True:
        button()
        text()
        exit()


if __name__ == "__main__":
    main()


