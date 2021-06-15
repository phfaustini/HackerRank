# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# DONE

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    values = set()
    subs = s[0]
    result = []
    for i, character in enumerate(s):
        values.add(ord(character)-96)
        if i > 0:
            if s[i-1] == character:
                subs += character
                values.add((ord(character)-96) * len(subs))
            else:
                subs = character
    for q in queries:
        if q in values:
            result.append("Yes")
        else:
            result.append("No")
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
