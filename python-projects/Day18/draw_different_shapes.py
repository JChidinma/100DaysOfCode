import turtle as T
import random

tim_the_turtle = T.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SeaGreen"]


def shape_draw(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        tim_the_turtle.forward(100)
        tim_the_turtle.right(angle)

    for num_shape_side in range(3, 11):  # triangle to Decagon shape
        tim_the_turtle.color(random.choice(colours))
        shape_draw(num_shape_side)
