# https://www.hackerrank.com/challenges/pairs
# DONE
from fileinput import input

n = k = None

for line in input():
    line = [int(i) for i in line.rstrip().split(" ")]
    if n is None:
        n = int(line[0])
        k = int(line[1])
    else:
        answer = 0

        line = sorted(line)
        i = 0
        j = 1
        while j < n:
            if line[j] - line[i] == k:
                answer+=1
                j+=1
            elif line[j] - line[i] < k:
                j+=1
            else:
                i+=1

        print(answer)