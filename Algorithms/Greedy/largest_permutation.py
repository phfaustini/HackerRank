# https://www.hackerrank.com/challenges/largest-permutation/problem
# 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


def largestPermutation(k, arr):
    sorted_arr = sorted(arr)
    i = 0
    pivot = 0
    while i < k and len(sorted_arr) > 0:
        maximum = sorted_arr.pop(-1)
        if maximum == arr[pivot]:
            pivot += 1
            continue
        swap(arr, pivot, arr.index(maximum))
        i += 1
        pivot += 1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
