'''Veer Khosla
CS151 A
Final Project
intro.py
'''

import turtle as t
import introText as it

LOOP = True

SCREEN = t.Screen()
SCREEN.setup(700, 600)
SCREEN.title('Introduction')
SCREEN.bgcolor('aliceblue')


def goto(t, x, y, heading):
    '''goes to any requested coordinates and sets any heading'''
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    t.hideturtle()


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
            print("Going to introText.py")
            it.main()

    t.onscreenclick(btnclick, 1)
    t.listen()


def tree(branchLen, t):
    '''draws tree using recursion'''
    if branchLen > 5:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen * 0.55, t)
        t.left(60)
        tree(branchLen * 0.55, t)
        t.right(30)
        t.backward(branchLen)


def treefunc():
    '''calls trees to the screen'''
    treeTurt = t.Turtle()
    treeTurt.width(5)
    treeTurt.left(90)
    treeTurt.up()
    treeTurt.backward(100)
    treeTurt.down()
    treeTurt.color("Black")
    x = -300
    for i in range(7):
        goto(treeTurt, x, -300, 90)
        tree(100,treeTurt)
        x += 100

    x = -300
    y = 350
    for i in range(7):
        goto(treeTurt, x, y, 270)
        tree(100,treeTurt)
        x += 100


def intro():
    '''writes out text'''
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.write("Learn about Climate Change!", font=("Arial", 20, "normal"))

    t.penup()
    t.goto(-333, 0)
    t.pendown()
    t.write("Press 'Next!' in the top right to continue and learn more!", font=("Arial", 20, "normal"))

    t.penup()
    t.goto(-275, -50)
    t.pendown()
    t.write("                 Press 'Q' at any time to exit.", font=("Arial", 20, "normal"))

    t.hideturtle()


def exit():
    '''exits function on "q" keypress'''
    t.listen()
    t.onkeypress(t.bye, 'q')
    t.listen()


def main():
    '''draws scene'''
    # t.resetscreen()
    intro()

    treefunc()
    while LOOP:
        button()
        exit()


if __name__ == '__main__':
    print('click Right Arrow to go to next scene or \'Q\' to exit')
    myTurtle = t.Turtle()
    myWin = t.Screen()
    main()
