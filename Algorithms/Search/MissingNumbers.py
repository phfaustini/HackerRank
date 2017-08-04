#https://www.hackerrank.com/challenges/missing-numbers
# Done
from fileinput import input

n = m = a = b = None

for line in input():
    line = line.rstrip()
    if n is None:
        n = int(line)
    elif a is None:
        a = [int(i) for i in line.split(" ")]
    elif m is None:
        m = int(line)
    else:
        b = [int(i) for i in line.split(" ")]
        a = sorted(a)
        b = sorted(b)

        stack = []

        sizeA = max(a)
        sizeB = max(b)
        size = max(sizeA, sizeB)
        arrayA = [0]*(size+1)
        arrayB = [0]*(size+1)
        for e in a:
            arrayA[e]+=1
        for e in b:
            arrayB[e]+=1

        for i in range(0, size+1):
            if arrayA[i] != arrayB[i]:
                if i not in stack: stack.append(i)
        stack = sorted(stack)
        
        for missing in stack:
            print(missing, end=" ")