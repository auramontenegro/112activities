#print lower left right-angled triangle
size = 7
for line in range (1, size + 1):
    for asterisk in range (1, line + 1):
        print ('*', end = '')
    print ()
