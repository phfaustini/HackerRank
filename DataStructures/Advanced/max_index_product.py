# https://www.hackerrank.com/challenges/find-maximum-index-product/problem


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def index_product(arr, pos):
    # pos: index of the target element
    if pos == 0 or pos == len(arr)-1:
        return 0

    index_left = 0
    for i in range(pos):
        if arr[i] > arr[pos]:
            index_left = i+1

    index_right = 0
    for i in range(pos+1, len(arr)):
        if arr[i] > arr[pos]:
            index_right = i+1
            break

    return index_left * index_right

def solve(arr):
    products = [index_product(arr, pos) for pos in range(len(arr))]
    return max(products)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
