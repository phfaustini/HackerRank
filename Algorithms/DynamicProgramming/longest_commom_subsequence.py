# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence

from fileinput import input


sizeFirst = None
sizeSecond = None
first = None
second = None
for line in input():
    line = line.rstrip()
    if sizeFirst is None:
        sizeFirst, sizeSecond = int(line.split(" ")[0]), int(line.split(" ")[1])
    elif first is None:
        first = line.split(" ")
    else:
        second = line.split(" ")
        matrix = [[0]*(sizeFirst+1)]*(sizeSecond+1)
        maximum = 0
        indexes = [0,0]
        for i in range(1, sizeFirst):
            for j in range(1, sizeSecond):
                if first[i] == second[j]:
                    matrix[i][j] = matrix[i-1][j-1]+1
                    if matrix[i][j] > maximum:
                        maximum = matrix[i][j]
                        indexes = [i,j]
        
        output = []
        while maximum >= 0:
            output.append(first[indexes[0]])
            maximum-=1
            indexes[0]-=1
        for i in range(len(output)-1, -1, -1):
            print(output[i], end=" ")