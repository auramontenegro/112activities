#Triangles with asterisks

#print lower left right-angled triangle
size = 7
for line in range (1, size + 1):
    for asterisk in range (1, line + 1):
        print ('*', end = '')
    print ()

#print lower right right-angled triangle
size = 7
for line in range (1, size + 1):
    for space in range (1, size - line + 1):
        print (' ', end = '')
    for asterisk in range (1, line + 1):
        print ('*', end = '')
        
    print ()
print()

#print upper left right-angled triangle
size = 7
for line in range (1, size + 1):
    for asterisk in range (1, size - line + 2):
        print ('*', end = '')
    print ()

#print upper right right-angled triangle
size = 7
for line in range (1, size + 1):
    for space in range (1, line + 1):
        print (' ', end = '')
    for asterisk in range (1, size - line + 2):
        print ('*', end = '')
        
    print ()
