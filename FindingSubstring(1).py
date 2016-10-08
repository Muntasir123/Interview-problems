from string import *
## Count the number of matches of a substring in a string
## "the" will result in 2 in the string "thestringthe"
def countSubStringMatch(target,key):
    start = 0
    count = 0
    pos = 0
    end = len(target)-1
    while(start < end):
        print pos
        pos = find(target,key,start)
        if pos != -1:
            count+=1
            start+=pos
    return count

print countSubStringMatch("atgacatgcacaagtatgcat","atgc")
        
