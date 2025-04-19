'''Veer Khosla
3/30/2023
CS151 A
Lab 6
lab6_snowman
'''

import graphicsPlus as gr
import time

def snowman_init(x, y, scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a snowman.
    Minimally, this is just three equal sized circles stack on top of each other
    with two smaller circles for the eyes

    Parameters:
    -----------
    x: int. x coordinate for the bottom circle center.
    y: int. y coordinate for the bottom circle center.
    scale: float. Scaled size of the snowman.

    Returns:
    -----------
    list with 5 Zelle Circle objects in it.
    '''

    radius = 30
    radiusEye = 3

    top = gr.Circle(gr.Point(x,y), radius)
    middle = gr.Circle(gr.Point(x, y+2*radius*scale), radius)
    bottom = gr.Circle(gr.Point(x, y+4*radius*scale), radius)
    eye1 = gr.Circle(gr.Point(x-scale*radius/2, y), radiusEye)
    eye2 = gr.Circle(gr.Point(x+scale*radius/2, y), radiusEye)

    shapes = [top, middle, bottom, eye1, eye2]
    return shapes


def snowman_animate(shapes, frame, win):
    '''Move the snowman at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the snowman
    frame: int. Current iteration of the animation
    win: GraphWin. Screen/canvas that the snowman is on'''

    if frame % 2 == 0:
        for shape in shapes:
            shape.move(10, 5) 
    if frame % 2 != 0:
        for shape in shapes:
            shape.move(-10, 5)
    
    for shape in shapes:
        shape.undraw()
        shape.draw(win)
    
        

def snowman_test():
    '''Main function that creates the screen, creates the snowman, draws it to the screen.
    '''
    width = 500
    height = 500

    win = gr.GraphWin('Snowman Animation', width, height)

    snowman = snowman_init(width/2, height/2, 1)
    for shape in snowman:
        shape.draw(win)


    for frame in range(1000):
        snowman_animate(snowman, frame, win)
        time.sleep(0.2)
        if win.checkMouse() is not None:
            break
    
    for shape in snowman:
        shape.undraw()
        shape.draw(win)


    win.getMouse()
    win.close()





if __name__ == "__main__":
    snowman_test()