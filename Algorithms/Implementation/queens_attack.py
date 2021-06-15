# https://www.hackerrank.com/challenges/queens-attack-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def in_obstacles(target, obstacles):
    i = 0
    for elem in obstacles:
        if elem == target:
            obstacles.pop(i)
            return True
        i += 1
    return False

def queensAttack(n, k, r_q, c_q, obstacles):
    legal_moves = 0
    #RIGHT
    for i in range(c_q + 1, n+1):
        if in_obstacles([r_q, i], obstacles):
            break
        legal_moves += 1
    #LEFT
    for i in range(c_q - 1 , 0, -1):
        if in_obstacles([r_q, i], obstacles):
            break
        legal_moves += 1
    # DOWN
    for i in range(r_q - 1 , 0, -1):
        if in_obstacles([i, c_q], obstacles):
            break
        legal_moves += 1
    # UP
    for i in range(r_q + 1 , n + 1):
        if in_obstacles([i, c_q], obstacles):
            break
        legal_moves += 1

    # DIAG UP LEFT
    i, j = r_q + 1, c_q - 1
    while i < n + 1 and j > 0:
        if in_obstacles([i, j], obstacles):
            break
        legal_moves += 1
        i += 1
        j -= 1
    # DIAG UP RIGHT
    i, j = r_q + 1, c_q + 1
    while i < n + 1 and j < n + 1:
        if in_obstacles([i, j], obstacles):
            break
        legal_moves += 1
        i += 1
        j += 1
    # DIAG DOWN RIGHT
    i, j = r_q - 1, c_q + 1
    while i > 0 and j < n + 1:
        if in_obstacles([i, j], obstacles):
            break
        legal_moves += 1
        i -= 1
        j += 1
    # DIAG DOWN LEFT
    i, j = r_q - 1, c_q - 1
    while i > 0 and j > 0 :
        if in_obstacles([i, j], obstacles):
            break
        legal_moves += 1
        i -= 1
        j -= 1
    
    return legal_moves
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
