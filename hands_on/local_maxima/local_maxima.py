import numpy as np

def local_maxima(numlist):
    loc = 0
    curr = numlist[0]
    for idx, elem in enumerate(numlist):
        if elem>curr:
            loc = idx
            curr = elem
    print(loc)
    return loc

#local_maxima([1, 3, -1, 2, 1])
