# Generate a random sequence of 10 numbers and sum them as an alternating series
# 1-2+3.. etc
from random import randint
random_arr = [ randint(0,99) for x in range(0,10)]
sum = 0
for i in range(0,10):
    add = lambda s: s+=random_arr[i]
    add(sum)

print sum
    
