#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
positives = 0
negatives = 0
zeroes = 0
for v in arr:
    if v > 0:
        positives+=1
    elif v < 0:
        negatives+=1
    else:
        zeroes+=1
print("%.6f\n%.6f\n%.6f" % (positives/n, negatives/n, zeroes/n))
