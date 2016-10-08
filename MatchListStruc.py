''' Given an array [1,[2,3],[4,[5,6]],7]
    And another array B = [2,3,4,5,6,7,8]
    Match the list struct in A in B. The output for this Example should be
    B = [2,[3,4],[4,[5,6]],7]

    Another example
    A = [4,5,[6,[7]]]
    B = [1,2,3,4]

    OUTPUT ~~~~
    B = [1,2,[3,[4]]]
    
''' 

def match(struct, source, index=0):
    if isinstance(struct, list):
        r = []
        for item in struct:
            next, index = match(item, source, index)
            r.append(next)
        return r, index
    else:
        return source[index], index + 1

A=[1,[2,3],[4,[5,6]],7]
B=[2,3,4,5,6,7,8]
print match(A, B)
