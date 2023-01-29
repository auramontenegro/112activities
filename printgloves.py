#Set up gloves variables
gloves1 = 10
gloves2 = 8
gloves3 = 3
gloves4 = 5


#Sales data into a list
gloves = [10,8,3,5]


#total in variables
totalvar = gloves1 + gloves2 + gloves3 + gloves4
print (totalvar)

#total in list
total = 0
for index in range (0,len(gloves)):
    total = total + gloves [index]
print (total)

#total in list with len(gloves)
totallen = 0
for index in range (len(gloves)):
    totallen = totallen + gloves [index]
print (totallen)


#reversing list
temp = gloves[0]
gloves[0] = gloves[3]
gloves[3] = temp
temp = gloves[1]
gloves[1] = gloves[2]
gloves[2] = temp
print(gloves)





