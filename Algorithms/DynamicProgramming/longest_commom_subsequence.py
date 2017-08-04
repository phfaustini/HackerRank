# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence
# DONE

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
        
        matrix = []
        for i in range(sizeFirst+1):
            matrix.append([])
            for j in range(sizeSecond+1):
                matrix[i].append(0)
        
        # Bulding matrix
        for i in range(1, sizeFirst+1):
            for j in range(1, sizeSecond+1):
                if first[i-1] == second[j-1]:
                    matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j]) + 1
                else:
                    matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
        
        # Backtracking
        i = sizeFirst
        j = sizeSecond
        output = ""
        while i >= 0 and j >= 0:
            if first[i-1] != second[j-1]:
                if matrix[i-1][j] > matrix[i][j-1]:
                    i-=1
                elif matrix[i-1][j] <= matrix[i][j-1]:
                    j -= 1
            else:
                i -= 1
                j -= 1
                output = str(first[i]) + " " + output
        print(output)
