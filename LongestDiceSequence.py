'''
A run is a sequence of adjacent repeated values. Write a program that generates a
sequence of 20 random die tosses and that prints the die values, marking the runs by
including them in parentheses, like this:
1 2 (5 5) 3 1 2 4 3 (2 2 2 2) 3 6 (5 5) 6 3 1

Now just like before get the Longest Run only So the output will be
1 2 5 5 3 2 1 4 3 (2 2 2 2) 3 6 5 5 6 3 1
Note you just find the first Longest Run should there be multiple
'''
from random import randint
arr = []
for i in range(1,21):
    rand_number = randint(1,6)
    arr.append(rand_number)

start_current = 0
length_current = 0
length_best = 0
start_best = 0

for i in range(0,19):
    if i == 0 or arr[i] == arr[i-1]:
        length_current = i - start_current + 1
        if length_current > length_best:
            length_best = length_current
            start_best = start_current
    else:
        start_current = i

arr.insert(start_best + length_best , ")")
arr.insert(start_best,"(")
for i in range(0,22):
    print arr[i],

            
            
            
        
        
        
    
    
