# Find the 1000th prime number
from math import sqrt
primeCount = 1
num = 1
while(primeCount < 1000):
    num+=2
    for k in range(2,1+int(sqrt(num+1))):
        if num%k ==0:
            break
    else:
        primeCount+=1
print num
            
