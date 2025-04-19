'''Veer Khosla
CS151 A
Project 8
arrangement.py'''

import lsystem
import turtle_interpreter
import turtle

def arrangement():
    '''draws flower arrangement'''
    tree1 = lsystem.Lsystem('tree1.txt')
    tree2 = lsystem.Lsystem('tree2.txt')
    tree3 = lsystem.Lsystem('tree3.txt')
    tree4 = lsystem.Lsystem('tree4.txt')

    draw = turtle_interpreter.TurtleInterpreter()

    str1 = tree1.buildString(3)
    str2 = tree2.buildString(3)
    str3 = tree3.buildString(3)
    str4 = tree4.buildString(2)

    draw.place(0, -100, 90)
    draw.setWidth(1.5)
    draw.drawString(str1, 15, 12)


    draw.setWidth(1)
    draw.place(0, -75, 130)
    draw.drawString(str2, 20, 20)
    draw.place(0, -75, 60)
    draw.drawString(str2, 20, 20)

    draw.place(0, -75, 150)
    draw.drawString(str2, 20, 20)
    draw.place(0, -75, 40)
    draw.drawString(str2, 20, 20)


    draw.setWidth(1.8)
    draw.place(0, -25, 130)
    draw.drawString(str4, 15, 15)
    draw.place(0, -25, 70)
    draw.drawString(str4, 15, 15)

    draw.place(0, -80, 170)
    draw.drawString(str4, 10, 15)
    draw.place(0, -80, 20)
    draw.drawString(str4, 10, 15)

    draw.place(-25, 50, 120)
    draw.drawString(str3, 10, 15)
    draw.place(25, 50, 80)
    draw.drawString(str3, 10, 15)

    turtle.hideturtle()
    turtle.update()
    turtle.exitonclick()


arrangement()
