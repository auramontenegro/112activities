#Draw a house
from turtle import *

#Draw a square
for sides in range (1, 5):
    forward(200)
    right(90)

#Draw a triangle on top
for sides in range (1, 4):
    forward(200)
    left(120)


#Draw door
penup()
right(90)
forward(200)
left(90)
forward(70)
left(90)
pendown()
for sides in range (1, 4):
    forward(60)
    right(90)

#Draw window
penup()
right(90)
forward(120)
right(90)
forward(20)
pendown()
for sides in range (1, 5):
    forward(40)
    right(90)
