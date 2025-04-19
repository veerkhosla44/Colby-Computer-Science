'''Daniel Tarkoff
CS151
4/18/2021
Project 08: Fractals and Trees
'''


import turtle
import sys
import lsystem22 as ls
import turtle_interpreter22 as it
import better_shapelib22 as bsl


def drawSnowFlake(x, y, size):
    '''Draws a snowflake centered @ x,y with size as parameter'''
    lsys = ls.init()
    ls.setBase(lsys, '[F]--[F]--[F]--[F]--[F]--[F]')
    # ls.addRule(lsys, ['F', 'FF[+F][-F]'])
    ls.addRule(lsys, ['F', 'FF[+F--F][-F++F][++F][--F]'])

    lstr = ls.buildString(lsys, 3)
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(x, y)
    turtle.pendown()
    it.drawString(lstr, size, 30)


def pyramid(x, y, size):
    '''Creates a pyramid positioned @ x,y with size as parameter'''
    lsys = ls.init()
    ls.setBase(lsys, 'F++F++F++')
    ls.addRule(lsys, ['F', 'F[+F][++F]F'])

    lstr = ls.buildString(lsys, 3)
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    it.drawString(lstr, size, 60)


def drawTreeShape(x, y, size):
    '''Creates a tree-shape positioned @ x,y with size as given parameter'''
    lsys = ls.init()
    ls.setBase(lsys, 'F')
    ls.addRule(lsys, ['F', 'FF[+F--F][-F++F][++F][--F]'])

    lstr = ls.buildString(lsys, 3)
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(x, y)
    turtle.pendown()
    it.drawString(lstr, size, 22)


def main(argv):
    '''Main function creating museum scene with three paintings'''
    bsl.museum_hallway('gold')
    bsl.painting_frame(-300,200,'gold')
    bsl.painting_frame(-75,200,'gold')
    bsl.painting_frame(150,200,'gold')
    drawSnowFlake(-225, 110, 3.5)
    pyramid(-60, 60, 15)
    drawTreeShape(225, 25, 8)
    turtle.exitonclick()


if __name__ == "__main__":
    turtle.tracer(False)
    turtle.hideturtle()
    main(sys.argv)
