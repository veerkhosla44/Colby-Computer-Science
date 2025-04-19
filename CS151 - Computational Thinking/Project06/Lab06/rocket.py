'''Veer Khosla
Spring 2023
Zelle Object Practice 
rocket.py'''

import graphicsPlus as gr

def init_rocket(x, y, scale):
    '''makes shapes of rocket'''
    shapes = []

    body_init = gr.Rectangle(gr.Point(x-scale*10, y), gr.Point(x+scale*10, y-scale*80))
    body_init.setFill('grey')
    shapes.append(body_init)

    nose_init = gr.Polygon(gr.Point(x-scale*10, y-scale*80), gr.Point(x, y-scale*100), gr.Point(x+scale*10, y-scale*80))
    nose_init.setFill(gr.color_rgb(150, 170, 200))
    shapes.append(nose_init)

    lfin_init = gr.Polygon(gr.Point(x-scale*10, y), gr.Point(x-scale*10, y-scale*20 ), gr.Point(x- scale*25, y+scale*5))
    lfin_init.setFill(gr.color_rgb(200, 170, 150))
    shapes.append(lfin_init)

    rfin_init = gr.Polygon(gr.Point(x+scale*10, y), gr.Point(x+scale*10, y-scale*20), gr.Point(x+scale*25, y+scale*5))
    rfin_init.setFill(gr.color_rgb(200, 170, 150))
    shapes.append(rfin_init)

    # clone the shapes before returning
    return shapes



