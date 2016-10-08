# Like before count substrings in string. Use recursion

from string import *
def countSubRecursive(target,key):
    index = 0
    count = 0
    index = find(target,key,index)
    if index != -1:
        count+=1
        index+=len(key)
        count+=countSubRecursive(target[index:],key)
    return count

print countSubRecursive("atgacatgcacaagtatgcat","atgc") 
