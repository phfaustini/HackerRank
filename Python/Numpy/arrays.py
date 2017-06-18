# https://www.hackerrank.com/challenges/np-arrays
# DONE

import numpy

def arrays(arr):
    arr = numpy.array([float(i) for i in arr], float)
    return (arr[::-1])    
    
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)