'''Veer Khosla
CS151 A
Project 8
growth.py'''

import turtle
import lsystem
import turtle_interpreter

class Art():
    draw = turtle_interpreter.TurtleInterpreter()


    def tree():
        'draws tree in middle of screen'
        tree = lsystem.Lsystem('growth1.txt')
        str = tree.buildString(3)

        Art.draw.place(0, -200, 90)
        Art.draw.setWidth(2)
        Art.draw.drawString(str, 10, 25.7)


    def shroomy():
        'draws circular shroom looking thing above tree in middle top of screen'
        shroomy = lsystem.Lsystem('growth2.txt')
        str2 = shroomy.buildString(2)
        heading = 90

        for i in range(8):
            Art.draw.place(0, 250, heading)
            Art.draw.setWidth(2)
            Art.draw.drawString(str2, 12, 27)
            heading += 45


    def fern():
        'draws fern on left side'
        fern = lsystem.Lsystem('growth3.txt')
        str3 = fern.buildString(3)
        str4 = fern.buildString(2)

        Art.draw.place(-300, -200, 90)
        Art.draw.setWidth(2)
        Art.draw.drawString(str3, 10, 22.5)

        Art.draw.place(-300, -100, 30)
        Art.draw.setWidth(2)
        Art.draw.drawString(str4, 10, 22.5)

        Art.draw.place(-300, -50, 50)
        Art.draw.setWidth(2)
        Art.draw.drawString(str4, 10, 22.5)


    def otherFern():
        'draws larger fern/plant on right side'
        shroomFern = lsystem.Lsystem('growth4.txt')
        str5 = shroomFern.buildString(2)
        str6 = shroomFern.buildString(3)
        str7 = shroomFern.buildString(4)

        heading = 90
        for i in range(8):
            Art.draw.place(250, 250, heading)
            Art.draw.setWidth(2)
            Art.draw.drawString(str5, 12, 27)
            heading += 45

        heading = 90
        for i in range(8):
            Art.draw.place(350, 100, heading)
            Art.draw.setWidth(2)
            Art.draw.drawString(str6, 12, 27)
            heading += 45


        heading = 90
        for i in range(8):
            Art.draw.place(300, -100, heading)
            Art.draw.setWidth(2)
            Art.draw.drawString(str7, 12, 27)
            heading += 45

        
        turtle.penup()
        turtle.goto(250, 250)
        turtle.goto(350, 100)
        turtle.pendown()
        turtle.pensize(4)
        turtle.circle(90.15, 155)

        turtle.penup()
        turtle.goto(300, -100)
        turtle.goto(350, 100)
        turtle.pendown()
        turtle.pensize(5)
        turtle.circle(125.1, 110)

        turtle.penup()
        turtle.goto(300, -100)
        turtle.pendown()
        turtle.setheading(270)
        turtle.fd(200)
        Art.draw.place(300, -300, 270)
        Art.draw.drawString(str6, 12, 27)


if __name__ == '__main__':
    turtle.bgcolor('lemonchiffon')

    Art.tree()
    Art.shroomy()
    Art.fern()
    Art.otherFern()

    turtle.hideturtle()
    turtle.update()
    turtle.exitonclick()
