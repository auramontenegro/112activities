#Produce graph for glove sales using loop
from turtle import *

#gloves list
gloves = [10,8,3,5]

#x axis
x = [20,40,60,80]

#Produce x axis
goto(80,0)

#Produce y axis
goto(0,0)
goto(0,100)

goto(0,0)
for index in range (len(gloves)):
    goto(20 + (20 * index), gloves[index] * 10)


#this one also works but uses an extra list
#for index in range (len(gloves)):
#    goto(x[index], gloves[index] * 10)
