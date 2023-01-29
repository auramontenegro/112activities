#Draw triangles across the page
from turtle import *
number_of_shapes = 4

for shape in range (1, number_of_shapes + 1):
    #Draw a triangle
    for sides in range (1, 4):
        forward(40)
        right(120)

    #Move forward to start position of next triangle
    penup()
    forward(50)
    pendown()
