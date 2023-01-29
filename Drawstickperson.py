#Draw stick person
from turtle import *

#Draw squared head
for sides in range (1, 5):
    forward(40)
    right(90)

#Move to start of torso
penup()
right(90)
forward(40)
left(90)
forward(20)
pendown()

#Draw torso
right(90)
forward(100)

#Draw legs
left(45)
forward(50)
penup()
right(180)
forward(50)
left(90)
pendown()
forward(50)

#Move to start of arms
penup()
right(135)
forward(80)
right(90)
pendown()
forward(80)
