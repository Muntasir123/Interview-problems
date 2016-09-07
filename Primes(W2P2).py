# Get the sum of the log of n primes, then divide it by n.
# Self- Check: Your answer should be getting converge to 1 for large n

from math import *
from math import sqrt
num = input("Enter the number we want to print out the sum of the logs of primes to ")
prime = 1
sum_log = log(2)
while(prime < num):
    prime+=2
    for k in range(2,1+int(sqrt(prime+1))):
        if prime%k == 0:
            break
    else:
        print "The prime is" + str(prime) + "and sum log is"
        sum_log+=log(prime)
print sum_log/num
 
