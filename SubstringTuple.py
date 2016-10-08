'''
Return a tuple of indices of where a specific substring matches
for example

subStringMatchExact("atgacatgcacaagtatgcat","atgc")
would return the tuple (5, 15).
'''

#We will use lists, since tuples are immutable and use more memory
# for insertion
from string import *
def subStringMatchExact(target,key):
    match_list = []
    start = 0
    pos = 0
    while start< len(target)-1:
        pos = find(target,key,start)
        if pos!= -1:
            start+= len(key) + pos
            match_list.append(pos)
    return tuple(match_list)

print subStringMatchExact("atgacatgcacaagtatgcat","atgc") 
