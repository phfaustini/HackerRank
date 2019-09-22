# https://www.hackerrank.com/challenges/the-best-aptitude-test/problem
# DONE
import numpy as np
from math import fabs

def arr2rank(arr):
    order = []
    for elem in arr:
        i = 0
        for j in arr:
            if elem > j:
                i += 1
        order.append(i)
    return order

def match(student_ranks, tests) -> int:
    student_ranks = arr2rank(student_ranks)
    i = 1
    t = 1
    minimum = np.inf
    for test in tests:
        test = arr2rank(test)
        s = sum(list(map(lambda x: fabs(x[0] - x[1]), list(zip(test, student_ranks)))))
        if s < minimum:
            minimum = s
            t = i
        i += 1
    return t

N = int(input())
while N > 0:
    n_students = int(input())
    student_ranks = list(map(float, input().rstrip().split()))
    tests = []
    for i in range(5):
        tests.append(list(map(float, input().rstrip().split())))
        n_students -= 1
    print(match(np.array(student_ranks), np.array(tests)))
    N -= 1
