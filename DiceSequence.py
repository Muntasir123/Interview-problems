'''
A run is a sequence of adjacent repeated values. Write a program that generates a
sequence of 20 random die tosses and that prints the die values, marking the runs by
including them in parentheses, like this:
1 2 (5 5) 3 1 2 4 3 (2 2 2 2) 3 6 (5 5) 6 3 1
'''
from random import randint
arr = []
for i in range(1,21):
    rand_number = randint(1,6)
    arr.append(rand_number)

in_run = False

for i in range(0,19):
    if in_run == True:
        if arr[i] != arr[i+1]:
            in_run = False
            print ")",
    else:
        if in_run == False:
            if arr[i] == arr[i+1]:
                in_run = True
                print "(",
    print arr[i],
        
    
    
