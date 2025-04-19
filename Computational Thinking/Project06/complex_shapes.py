'''Veer Khosla
3/30/2023
CS151 A
Project 6
complex_shapes.py
'''

import graphicsPlus as gr


def draw (shapes, win):
    '''A for loop that draws each item in the given list of shapes'''
    for item in shapes:
        item.draw(win)


def iceberg_init(x, y, scale):
    '''makes iceberg which bear sits on'''
    iceberg_shapes = []

    # iceberg_face1 = gr.Polygon(gr.Point(300, 300), gr.Point(470, 300), gr.Point(350, 430), gr.Point(250, 400))
    iceberg_face1 = gr.Polygon(gr.Point(x, y), gr.Point(x + 170 * scale, y), gr.Point(x + 50 * scale, y + 130 * scale), gr.Point(x - 50 * scale, y + 100 * scale))
    iceberg_face1.setFill(gr.color_rgb(226,237,246))
    iceberg_face1.setWidth(4)
    iceberg_face1.setOutline(gr.color_rgb(226,237,246))

    # iceberg_face2 = gr.Polygon(gr.Point(350, 430), gr.Point(500, 400), gr.Point(470, 300), gr.Point(380, 300))
    iceberg_face2 = gr.Polygon(gr.Point(x + 50 * scale, y + 130 * scale), gr.Point(x + 200 * scale, y + 100 * scale), gr.Point(x + 170 * scale, y), gr.Point(x + 80 * scale, y))
    iceberg_face2.setFill(gr.color_rgb(246, 246, 255))
    iceberg_face2.setWidth(4)
    iceberg_face2.setOutline(gr.color_rgb(246, 246, 255))

    iceberg_shapes.append(iceberg_face2)
    iceberg_shapes.append(iceberg_face1)

    return iceberg_shapes


def crate_init(x, y, scale):
    '''makes the green crates floating in the water'''
    crate_shapes = []

    crate_face1 = gr.Polygon(gr.Point(x + 50 * scale, y), gr.Point(x + 70 * scale, y - 20 * scale), gr.Point(x + 50 * scale, y - 50 * scale), gr.Point(x + 30 * scale, y - 30 * scale))
    crate_face1.setFill('green')
    crate_face1.setOutline('darkgreen')
    crate_face1.setWidth(3)
    crate_shapes.append(crate_face1)

    crate_face2 = gr.Polygon(gr.Point(x, y), gr.Point(x + 50 * scale, y), gr.Point(x + 30 * scale, y - 30 * scale))
    crate_face2.setFill('green')
    crate_face2.setOutline('darkgreen')
    crate_face2.setWidth(3)
    crate_shapes.append(crate_face2)
    
    return crate_shapes


def barrel_init(x, y, scale):
    '''makes red barrels floating in the water'''
    barrel_shapes = []

    barrel_length = gr.Polygon(gr.Point(x, y - 25 * scale), gr.Point(x + 25 * scale, y), gr.Point(x + 75 * scale, y + 15 * scale))
    barrel_length.setFill(gr.color_rgb(209, 92, 92))
    barrel_length.setOutline('darkred')
    barrel_length.setWidth(3)
    barrel_shapes.append(barrel_length)

    barrel_length2 = gr.Polygon(gr.Point(x, y + 25 * scale), gr.Point(x + 25 * scale, y), gr.Point(x + 75 * scale, y + 15 * scale))
    barrel_length2.setFill(gr.color_rgb(209, 92, 92))
    barrel_length2.setOutline('darkred')
    barrel_length2.setWidth(3)
    barrel_shapes.append(barrel_length2)

    barrel_base = gr.Circle(gr.Point(x, y), 25 * scale)
    barrel_base.setFill(gr.color_rgb(209, 92, 92))
    barrel_base.setOutline('darkred')
    barrel_base.setWidth(3)
    barrel_shapes.append(barrel_base)

    return barrel_shapes
