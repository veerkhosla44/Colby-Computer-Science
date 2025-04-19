'''Veer Khosla
Spring 2023
Zelle Object Practice 
rocket.py'''

import graphicsPlus as gr
import rocket as r
import time

def main():
    # Create a GraphWin window that is at least 400 x 400
    win = gr.GraphWin("Rocket", 1000, 700)
    
    # assign to rocket1 the result of calling init_rocket with arguments 100, 300, 1
    rocket1 = r.init_rocket(100, 600, 1)
    rocket2 = r.init_rocket(190, 600, 1.5)
    rocket3 = r.init_rocket(300, 600, 2)

    # for each shape in rocket1
    for shape in rocket1:
        shape.draw(win)

    for shape in rocket2:
        shape.draw(win)

    for shape in rocket3:
        shape.draw(win)

    for i in range(1000):
        for shape in rocket1:
            shape.move(0, -1)
        for shape in rocket2:
            shape.move(0, -1)
        for shape in rocket3:
            shape.move(0, -1)

    for shape in rocket1:
        shape.undraw()
        shape.draw(win)

    # time.sleep(0.05)


    # wait for a mouse click
    win.getMouse()
    # close the window
    win.close()

if __name__ == "__main__":
    main()