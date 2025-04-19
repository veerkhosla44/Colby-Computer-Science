
import shapelib
import turtle

def tree(x_position, y_position, scale):
    shapelib.tammy.up()
    shapelib.tammy.goto(x_position, y_position)
    shapelib.tammy.down()

    shapelib.rectangle(40 * scale, 100 * scale, "brown")
    shapelib.tammy.up()
    shapelib.tammy.goto((-30  * scale + x_position), (100* scale + y_position ) )
    shapelib.tammy.down()
    shapelib.triangle(100* scale, "green")


def main():
    
    tree(-200, -300, 3)
    tree(0, 0, 1)
    tree(100, 140, 0.7)
    tree(200, 230, 0.5)
    
    turtle.exitonclick()

main()