from fileinput import input
for line in input():
    occurrences = [0]*123
    line = line.rstrip()
    for char in line:
        occurrences[ord(char)]+=1
    while 0 in occurrences:
        occurrences.remove(0)
    minimum = min(occurrences)
    maximum = max(occurrences)
    if minimum == maximum:
        print("YES")
    elif maximum - minimum > 1:
        print("NO")
    else:
        for i in range(0, len(occurrences)):
            aux = occurrences[:]
            exi = False
            while(aux[i] > 0):
                aux[i] -= 1
                if aux[i] == 0: aux.pop(i)
                minimum = min(aux)
                maximum = max(aux)
                if minimum == maximum:
                    exi=True
                    print("YES")
                    break
            if exi: break
        else:
            print("NO")
