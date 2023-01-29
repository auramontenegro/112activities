#Draw squares across page of increasing size
from turtle import *
number_of_shapes = 4

for shape in range (1, number_of_shapes + 1):
    #Draw a square
    for sides in range (1, 5):
        forward(30 + shape * 10)
        right(90)

    #Move forward to start position of next square
    penup()
    forward(40 + shape *10)
    pendown()
