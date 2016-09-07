'''

It is a well-researched fact that men in a restroom generally prefer to maximize their
distance from already occupied stalls, by occupying the middle of the longest
sequence of unoccupied places.
For example, consider the situation where ten stalls are empty.
_ _ _ _ _ _ _ _ _ _
The first visitor will occupy a middle position:
_ _ _ _ _ X _ _ _ _


'''

stalls = []

def give_stalls(b):
    for i in range(0,10):
        b.append(False)

def insert_stall(b):
    for i in range(0,10):
        if b[i] == False:
            b[i] = "_"
        else:
            b[i] = "X"
            
give_stalls(stalls)
insert_stall(stalls)
print stalls


        
