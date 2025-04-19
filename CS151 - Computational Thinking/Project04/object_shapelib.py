'''Veer Khosla
CS151 A
3/8/2023
Project 04
object_shapelib.py'''

import turtle as t


def goto(turt, x, y, heading = 0): 
    '''this function moves turtle to any location'''
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.setheading(heading)

    return turt


def circle(turt, x ,y, radius, angle = 360, penWidth = 3, fill = True, fillColor = 'brown', heading = 0):
    'this function makes a circle of any radius and angle at any location. Fills if True and takes input for color and heading'
    turt.speed(0)
    goto(turt, x, y, heading)
    turt.pensize(penWidth)
    turt.pencolor('black')
    
    
    if fill:
        turt.fillcolor(fillColor)
        turt.begin_fill()
        turt.circle(radius, angle)
        turt.end_fill()
    else:
        turt.circle(radius, angle)

    turt.hideturtle()
    return turt
    

def straights(turt, x , y, length, penWidth = 3, fill = True, fillColor = 'brown', heading = 0):
    '''this function makes the straights in my race track. It makes a rectangle of any length at any location and fills if True. Same arguments for color and heading'''
    goto(turt, x, y, 0)
    turt.fillcolor(fillColor)
    turt.begin_fill()


    for i in range(2):
        turt.pencolor('black')
        turt.forward(length)
        turt.right(90)
        turt.pencolor(fillColor)
        turt.forward(65)
        turt.right(90)

    turt.end_fill()
    turt.hideturtle()


def laneTurns(turt, x ,y, radius, angle = 360, penWidth = 3, fill = True, fillColor = 'brown', heading = 0):
    '''draws the turns of the track'''
    turt.speed(0)
    goto(turt, x, y, heading)
    turt.pensize(penWidth)
    turt.pencolor('white')

    turt.circle(radius, angle)

    turt.hideturtle()
    return turt


def laneStraights(turt, x , y, length, penWidth = 3, fill = True, fillColor = 'brown', heading = 0):
    '''draws the straights of the track'''
    goto(turt, x, y, 0)
    turt.forward(length)
    turt.hideturtle()


#EXTENSION FUNCTIONS:
def straightsExtension(turt, x , y, length, penWidth = 3, fill = True, fillColor = 'brown', heading = 0):
    '''this function makes the straights in my race track. It makes a rectangle of any length at any location and fills if True. Same arguments for color and heading'''
    goto(turt, x, y, 0)
    turt.fillcolor(fillColor)
    turt.begin_fill()


    for i in range(2):
        turt.pencolor('black')
        turt.forward(length)
        turt.right(90)
        turt.pencolor(fillColor)
        turt.forward(40)
        turt.right(90)

    turt.end_fill()
    turt.hideturtle()


def boards():
    '''draws scoreboards'''
    t.penup()
    t.goto(-420, 225)
    t.pendown()
    t.setheading(0)
    t.color('black', 'black')
    t.begin_fill()

    for i in range(2):
        t.fd(180)
        t.left(90)
        t.fd(100)
        t.left(90)

    t.end_fill()
    t.penup()
    t.goto(-330, 225)
    t.pendown()
    t.setheading(270)
    t.pensize(10)
    t.fd(50)

    t.penup()
    t.goto(230, 225)
    t.pendown()
    t.setheading(0)
    t.color('black', 'black')
    t.begin_fill()

    for i in range(2):
        t.fd(200)
        t.left(90)
        t.fd(100)
        t.left(90)

    t.end_fill()

    t.penup()
    t.goto(330, 225)
    t.pendown()
    t.setheading(270)
    t.pensize(10)
    t.fd(50)
        

#RACE TRACK:
def draw_race_scene(width, height, title, color = 'white'):
    '''This function makes an object which draws my scene'''
    
    screen = t.Screen()

    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor(color)

    track = t.Turtle()
    
    #TRACK
    circle(track, 150, 0, 100, 180, 3, True, 'brown')
    circle(track, 150, 65, 35, 180, 3, True, color)
    
    straights(track, -150, 200, 300, 3, True)
    straights(track, -150, 65, 300, 3, True)

    circle(track, -150, 200, 100, 180, 3, True, 'brown', 180)
    circle(track, -150, 135, 35, 180, 3, True, color, 180)


    #LANES 
    laneTurns(track, 150, 25, 75, 180, 1.5, False, 'white')
    
    laneStraights(track, -150, 175, 300, 1.5, False)
    laneStraights(track, -150, 25, 300, 1.5, False)

    laneTurns(track, -150, 175, 75, 180, 1.5, False, 'white', 180)


    # EXTENSION ADDITIONS
    straightsExtension(track, -200, 400, 400, 3, True, 'grey')
    straightsExtension(track, -150, 350, 300, 3, True, 'grey')
    straightsExtension(track, -100, 300, 200, 3, True, 'grey')
    
    boards()

    track.hideturtle()


# if __name__ == '__main__':
#     draw_race_scene(1000, 800, 'Race Track', 'green')

# t.exitonclick()


