'''Veer Khosla
CS151 A
2/22/23
Project 03
better_shapelib.py'''

import random as r
import turtle as t
import math as m

def goto(x, y): 
    '''this function moves turtle to any location'''
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)


# Functions for Mondrian Pattern:
def rectangle(x, y, width, height, fillColor, edgeColor = 'black', fill = False, penWidth = 1, s = 1):
    '''Draws a rectangle at coordinates (x, y) of given width and height, edge color, fill color, and pen size'''
    goto(x, y)

    t.pencolor('black')

    if fill == True:
        t.pensize(2)
        t.begin_fill()
        t.color(edgeColor, fillColor)

        for i in range(2):
            t.forward(width * s)
            t.left(90)
            t.forward(height * s)
            t.left(90)    

        t.end_fill()

    else:
        for i in range(2):
            t.pensize(penWidth)
            t.color('black', 'black')

            t.forward(width * s)
            t.left(90)
            t.forward(height * s)
            t.left(90)

    t.pencolor('black')
    t.pensize(1)


def rectanglePattern(s, numRect = 200):
    '''this function generates a given number rectangles of random color, size, and location'''

    for i in range(numRect):
        rgb1 = r.random()
        rgb2 = r.random()
        rgb3 = r.random()

        fillColor = (rgb1, rgb2, rgb3)

        if i <= 80:
            rectangle(r.randint(400, 520)*s, r.randint(60, 160)*s, r.randint(50, 150), r.randint(50, 150), fillColor, 'black', True, 2, 0.1)

        else:
            rectangle(r.randint(400, 520)*s, r.randint(60, 160)*s, r.randint(50, 150), r.randint(50, 150), fillColor, 'black', False, 2, 0.1)


def mountain(x, y, width, height, fillColor, edgeColor = 'black', fill = False, penWidth = 1):
    '''Draws a triangle at coordinates (x, y) of given width and height, edge color, fill color, and pen size'''
    goto(x, y)

    t.pencolor('black')

    hypo = m.sqrt( (width/2)**2 + (height**2) )
    angleA = m.degrees(m.asin(height / hypo))
    angleB = 2 * m.degrees(m.asin((width/2) / hypo))

    if fill == True:
        t.pensize(2)
        t.begin_fill()
        t.color(edgeColor, fillColor)

        t.forward(width)
        t.left(180 - angleA)
        t.forward(hypo)
        t.left(180 - angleB)
        t.forward(hypo) 

        t.end_fill()

    else:
        t.pensize(penWidth)

        t.forward(width)
        t.left(180 - angleA)
        t.forward(hypo)
        t.left(180 - angleB)
        t.forward(hypo) 

    t.pencolor('black')
    t.pensize(1)


def mountainPattern(x = 500, y = 500, s = 1, numShapes = 150):
    '''this function generates a given number of triangles of random color, size, and location, within the parameters'''


    for i in range(numShapes):

            # rgb1 = r.random()
            # rgb2 = r.random()
            # rgb3 = r.random()

            rgbR = r.randint(45, 250)
            rgbG = rgbR
            rgbB = rgbG

            fillColor = (rgbR/255, rgbG/255, rgbB/255)

            mountain(r.randint(-x, x) * s, 50 * s, r.randint(50, 150) * s, r.randint(50, 200) * s, fillColor, 'black', True)




        # if i < numShapes/3:
        #     mountain(r.randint(-x, x) * s, r.randint(50, y) * s, r.randint(50, 150) * s, r.randint(50, 150) * s, fillColor, 'black', True)

        # else:
        #     mountain(r.randint(-x, x) * s, r.randint(50, y) * s, r.randint(50, 150) * s, r.randint(50, 150) * s, fillColor, 'black', False, 2)

# STEP 4:

#   Simple Shape 1 from Project 2 - Star:
def starSun (x, y, length, fill = r.choice([True, False])):
        '''Draws 10-sided orange star'''

        goto(x, y)
        t.setheading(0)

        if fill == False:
            for i in range(10):
                for i in range(5):
                    t.forward(length*1.3)
                    t.right(144)
                t.right(36)
            return length
        else:
            t.begin_fill()
            t.color('orange')
            for i in range(10):
                for i in range(5):
                    t.forward(length*1.3)
                    t.right(144)

                t.right(36)
            t.end_fill()
            return length
        

#   Simple Shape 2 from Project 2 - Circle
def circleSun(x, y, radius, fill = r.choice([True, False])):
        '''Draws a dark orange circle at (x, y) with given radius'''

        goto(x, y - radius)
        t.setheading(0)

        if fill == False:
            t.circle(radius)
        else:
            t.begin_fill()
            t.color('darkorange')
            t.circle(radius)
            t.end_fill()

# STEP 5:
#   FULL SCENE FROM PROJECT 2 - SUNSET OVER THE WATER:
def outdoor_scene1(x, y, s, fill = True):
    '''this function creates an outdoor scene based on my selected image by calling many functions in a specific order'''

    def rectangle(x, y, scale, color):
        '''this function makes a rectangle of any color at any given coordinates'''
        goto(x, y)
        if color == 'green':
            t.setheading(0)

        t.pencolor(color)
        t.begin_fill()
        t.fillcolor(color)

        for i in range(2):
            t.forward(200*scale)
            t.left(90)
            t.forward(400*scale)
            t.left(90)

        t.end_fill()


    def grassOrWater(x, y, sideLength1, sideLength2, color):
        '''this function draws triangles with any given side lengths and color, at any given coordinates'''

        t.penup()
        t.goto(x, y)
        
        if color == 'green':
            t.setheading(0)
        t.pendown()

        hypo = m.sqrt(sideLength1**2 + sideLength2**2)
        angleA = m.degrees(m.asin(sideLength2 / hypo))
        angleB = m.degrees(m.asin(sideLength1 / hypo))

        t.pencolor(color)
        t.fillcolor(color)
        t.begin_fill()

        t.forward(sideLength1)
        t.left(180 - angleA)
        t.forward(hypo)
        t.left(180 - angleB)
        t.forward(sideLength2)


        t.end_fill()
        t.penup()


    def sky(x, y, fill = r.choice([True, False])):
        '''this function draws the sky with different coordinates and color arguments from the skyRectangle function'''

        def skyRectangle(x, y, color):
            '''this function makes a rectangle of a given color at any given coordinates for the sky.'''
            if fill == False:
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.setheading(0)

                for i in range(2):
                    t.forward(950*s)
                    t.left(90)
                    t.forward(25*s)
                    t.left(90)

            else:
                t.penup()
                t.goto(x*s, y*s)
                t.pendown()
                t.setheading(0)
                t.pencolor(color)
                t.begin_fill()
                t.fillcolor(color)

                for i in range(2):
                    t.forward(950*s)
                    t.left(90)
                    t.forward(25*s)
                    t.left(90)

                t.end_fill()


        def skyBlueRectangle(x, y):
            '''this function makes a rectangle that is large and blue at any given coordinates as part of the sky'''
            if fill == False:
                t.penup()
                t.goto(x*s, y*s)
                t.pendown()

                for i in range(2):
                    t.forward(950*s)
                    t.left(90)
                    t.forward(200*s)
                    t.left(90)

            else:
                t.penup()
                t.goto(x*s, y*s)
                t.pendown()

                t.pencolor('dodgerblue')
                t.begin_fill()
                t.fillcolor('dodgerblue')

                for i in range(2):
                    t.forward(950*s)
                    t.left(90)
                    t.forward(200*s)
                    t.left(90)

                t.end_fill()
        
        
        y = y*s
        colors = ['darkorange1', 'gold', 'lightgoldenrod1', 'khaki1', 'paleturquoise1', 'skyblue1', 'deepskyblue']
    
        for color in colors:
            skyRectangle(x, y, color)
            y += 25
        skyBlueRectangle(x, y)


    def sun(x, y, radius, fill):
        '''this function calls the starSun and circleSun functions to create a more detailed sun by overlaying the circle over the star.'''
        starSun(x, y, radius, True)
        circleSun(x, y, radius, True)


    grassOrWater((-425+x*s)*s, (-350+y*s)*s, 800*s, 450*s, 'green')
    t.pendown()

    t.left(270)
    grassOrWater((325+x*s)*s, (50+y*s)*s, 750*s, 400*s,  'blue')

    rectangle((325+x*s)*s, (-350+y*s)*s, s, 'green')
    t.left(90)
    rectangle((325+x*s)*s, (-350+y*s)*s, 0.5*s, 'lightgoldenrod3')

    if y < 0:
        sky((-425/s + x)*s, (50/s + y/s)*s, True)
    elif y >= 0:
        sky((-425/s + x)*s, (50/s + y/s)*s, True)


    t.pencolor('orange')
    
    sun((-300 + x*s)*s, (215 + y*s)*s, 50*s, True)
    

#   PATTERN OF SCENE FROM PROJECT 2 - 3 SUNSETS:
def pattern_outdoorScene(x, y, s):
    '''calls function outdoor_scene1 from project 2 3x, at different positions and scales'''

    outdoor_scene1(-800*s, 900*s, 0.4*s)
    outdoor_scene1(1200*s, -2000*s, 0.3*s)
    outdoor_scene1(5000*s, 5000*s, 0.2*s)


# Functions for OutdoorScene:
def frame(x, y, length, width, edgeColor = 'black', fillColor = 'black' , fill = False):
    '''Draws a rectangle of any size at any position with option to fill and change color if fill = True'''
    t.pensize(10)
    t.color('black')
    goto(x, y)
    t.pendown()


    if fill == False:
        for i in range(2):
            t.forward(length)
            t.left(90)
            t.forward(width)
            t.left(90)
    else:
        t.pencolor(edgeColor)
        t.pensize(3)
        t.fillcolor(fillColor)
        t.begin_fill()

        for i in range(2):
            t.forward(length)
            t.left(90)
            t.forward(width)
            t.left(90)

        t.end_fill()
        

def floor():
    '''Draws large rectangle of brownish color as the floor'''
    t.pendown()
    goto(-450, -50)
    t.color('chocolate4')
    t.fillcolor('chocolate4')
    t.begin_fill()

    for i in range(2):
        t.forward(900)
        t.right(90)
        t.forward(500)
        t.right(90)
    
    t.end_fill()


def curtainRod():
    '''draws a dark grey line of thick pensize'''
    goto(-200, 225)
    t.pensize(8)
    t.color('darkgrey')
    t.pendown()
    t.forward(450)


def carpet(x, y):
    '''draws dark grey trapezoid as carpet - trapezoid shape helps the scene look 3D '''
    t.fillcolor('darkgrey')
    t.begin_fill()

    goto(x, y)
    t.color('darkgrey')
    t.forward(400)
    t.right(65)
    t.forward(200)

    t.right(115)
    t.forward(570)
    t.right(115)
    t.forward(200)


    t.end_fill()


def carpetDesign():
        '''draws the semi-circle designs on the carpet'''
    
        x = -190
        for i in range(25):
            x += 15
            goto(x, -125)
            t.pensize(2)
            t.color('slategrey')
            t.circle(7.5, 180)


        x = -190
        for i in range(25):
            x += 15
            goto(x, -125)
            t.setheading(180)
            t.pensize(2)
            t.color('slategrey')
            t.circle(7.5, 180)

        x = -220
        for i in range(28):
            x += 15
            goto(x, -165)
            t.pensize(2)
            t.color('slategrey')
            t.circle(7.5, 180)

        x = -220
        for i in range(28):
            x += 15
            goto(x, -165)
            t.setheading(180)
            t.pensize(2)
            t.color('slategrey')
            t.circle(7.5, 180)

        x = -235
        for i in range(30):
            x += 15
            goto(x, -205)
            t.pensize(2)
            t.color('slategrey')
            t.circle(7.5, 180)

        x = -235
        for i in range(30):
            x += 15
            goto(x, -205)
            t.setheading(180)
            t.pensize(2)
            t.color('slategrey')
            t.circle(7.5, 180)

        x = -250
        for i in range(32):
            x += 15
            goto(x, -245)
            t.pensize(2)
            t.color('slategrey')
            t.circle(7.5, 180)

        x = -250
        for i in range(32):
            x += 15
            goto(x, -245)
            t.setheading(180)
            t.pensize(2)
            t.color('slategrey')
            t.circle(7.5, 180)


def moon(x, y, radius):
    '''Draws a white circle at any given coordinates with any given radius'''

    goto(x, y - radius)
    t.setheading(0)

    t.begin_fill()
    t.color('white')
    t.circle(radius)
    t.end_fill()



# Uncomment below to test Required Image 2:

# t.tracer(False)

# if __name__ == '__main__':
#     pattern_outdoorScene(0, 0, 1)

# t.exitonclick()