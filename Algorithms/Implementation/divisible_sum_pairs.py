# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# DONE
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = map(int, raw_input().rstrip().split())

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
