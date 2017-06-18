# https://www.hackerrank.com/challenges/sherlock-and-valid-string
# DONE

from fileinput import input
for line in input():
    occurrences = [0]*26
    line = line.rstrip()
    for char in line:
        i = ord(char) - 97
        occurrences[ i ] += 1
    while 0 in occurrences:
        occurrences.remove(0)
    minimum = min(occurrences)
    maximum = max(occurrences)
    if minimum == maximum:
        print("YES")
    else:
        for i in range(0, len(occurrences)):
            aux = occurrences[:]
            aux[i] -= 1
            if aux[i] == 0: aux.pop(i)
            minimum = min(aux)
            maximum = max(aux)
            if minimum == maximum:
                print("YES")
                break
        else:
            print("NO")