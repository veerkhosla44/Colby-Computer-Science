'''Veer Khosla
CS151 A
Spring 2023
main.py
2/9/2023
This file stores functions written to draw scene for Project 2'''

import turtle as t
import shapelib as sl
import random as r
t.speed(500)

t.tracer(False)

def outdoor_scene1():
    '''this function creates an outdoor scene based on my selected image by
    putting all my functions from shapelib.py together :)'''
    sl.grassOrWater(-425, -350, 800, 450, 'green')
    t.pendown()

    t.left(270)
    sl.grassOrWater(325, 50, 750, 400,  'blue')

    sl.rectangle(325, -350, 1, 'green')
    t.left(90)
    sl.rectangle(325, -350, 0.5, 'lightgoldenrod3')

    sl.sky()
    
    sl.sun(-300, 115, 50)


# y: no lower than 115
def extensionRandomness():
    '''DOC STRING'''

    i = r.randint(1,2)

    if i == 1:
        sl.grassOrWater(-425, -350, 800, 450, 'green')
        t.pendown()

        t.left(270)
        sl.grassOrWater(325, 50, 750, 400,  'blue')

        sl.rectangle(325, -350, 1, 'green')
        t.left(90)
        sl.rectangle(325, -350, 0.5, 'lightgoldenrod3')

        sl.sky()

        sl.sunRandom()

    else:
        sl.grassOrWater(-425, -350, 800, 450, 'green')
        t.pendown()

        t.left(270)
        sl.grassOrWater(325, 50, 750, 400,  'blue')

        sl.rectangle(325, -350, 1, 'green')
        t.left(90)
        sl.rectangle(325, -350, 0.5, 'lightgoldenrod3')
            
        sl.nightSky()
        sl.stars()
        sl.moonRandom()

    
    
    
# PROJECT MAIN CODE FUNCTION CALLS

# sl.starSun(-300, 115, 50)
# sl.circleSun(-300, 115, 50)
# sl.sun(-300, 115, 50)
# sl.sky()

outdoor_scene1()

# EXTENSION MAIN CODE
# extensionRandomness()

t.exitonclick()


