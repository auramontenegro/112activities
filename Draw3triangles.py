
#Draw 3 triangles
from turtle import *

#Draw triangle 1
for sides in range (1, 4):
    forward(40)
    left(120)

	
#Move to start of triangle 2
penup()
left(90)
forward(100)
right(90)
pendown()

#Draw triangle 2
for sides in range (1, 4):
    forward(40)
    left(120)

#Move to start of triangle 3
penup()
forward(100)
right(90)
forward(100)
left(90)
pendown()
 
#Draw triangle 3
for sides in range (1, 4):
    forward(40)
    left(120)

	
