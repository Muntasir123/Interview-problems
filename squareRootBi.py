'''
create your own square root function
Here I will solve this using the Bisection method.
'''

def squareRootBi(x,epsilon):
    assert epsilon > 0, 'episilon must be positive,not' + str(epsilon)
    low = 0
    high = max(x,1)
    guess = (low+high) / 2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low+high)/2.0
        print guess, ctr
        ctr+=1
    return guess

print squareRootBi(100,0.01)
