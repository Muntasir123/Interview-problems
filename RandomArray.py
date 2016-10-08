'''
Write a program that produces random permutations of the numbers 1 to 10. To
generate a random permutation, you need to fill an array with the numbers 1 to 10
so that no two entries of the array have the same contents.
Muntasir Alam
'''
from random import randint

# Fill another array with 1-10, then simply push that inside the resultant array
# this is better than a potential O(N^2) for brute force

x = [i for i in range(1,11)]
rslt = []
for i in range(0,10):
    pos = randint(0,9-i)
    print pos
    rslt.append(x[pos])
    x.pop(pos)

# We could probably shuffle indexes with the shuffle() method
    

