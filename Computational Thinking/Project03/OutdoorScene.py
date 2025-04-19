'''Veer Khosla
CS151 A
2/22/23
Project 03
OutdoorScene.py'''

import turtle as t
import better_shapelib as bsl
import sys

def outdoorScene():
    '''Calls functions from better_shapelib to make a new scene with other scenes inside.

    COMMAND LINE CONTROLS: type 'python OutdoorScene.py', followed by  '0' or '1' to change the time of day out the window.
        - 0 = day; 1 = night; else = error
        - If using OSX, only difference is 'python3' instead of 'python'
    
        - ex: 'python(3) OutdoorScene.py 0' for day'''
    
    time = int(sys.argv[1])

    day = 0
    night = 1

    bsl.outdoor_scene1(-20000, 5000, 0.13)
    

    bsl.frame(-390, 40, 120, 100)
    bsl.frame(280, 40, 100, 90, 'black', 'white', True)
    bsl.rectanglePattern(0.7, 150)

    if time == day:
        bsl.frame(-175, 25, 400, 200, 'white', 'skyblue', True)
        bsl.starSun(-100, 190, 20, True)
        bsl.circleSun(-100, 190, 20, True)

        bsl.curtainRod()
        bsl.floor()

        bsl.carpet(-190, -100)
        bsl.carpetDesign()


        bsl.mountainPattern(315, 200, 0.5, 300)
        bsl.frame(-200, -15, 50, 240, 'cornsilk', 'cornsilk', True)
        bsl.frame(200, -15, 50, 240, 'cornsilk', 'cornsilk', True)

        t.bgcolor('burlywood')

        t.exitonclick()
    elif time == night:
        bsl.frame(-175, 25, 400, 200, 'white', 'black', True)
        bsl.moon(100, 190, 20)

        bsl.curtainRod()
        bsl.floor()

        bsl.carpet(-190, -100)
        bsl.carpetDesign()


        bsl.mountainPattern(315, 200, 0.5, 300)
        bsl.frame(-200, -15, 50, 240, 'cornsilk', 'cornsilk', True)
        bsl.frame(200, -15, 50, 240, 'cornsilk', 'cornsilk', True)

        t.bgcolor('burlywood')

        t.exitonclick()
    else:
        print('***ERROR: Please enter either 0 or 1 for day or night, respectively***')
        t.bye()


t.tracer(False)

if __name__ == '__main__':
    outdoorScene()





