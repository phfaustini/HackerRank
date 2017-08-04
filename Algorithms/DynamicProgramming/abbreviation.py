#https://www.hackerrank.com/challenges/abbr
# Fails case 11
from fileinput import input

tests = None
a = None
b = None
for line in input():
    line = line.rstrip()
    if tests is None:
        tests = int(line)
    elif a is None:
        a = line
    else:
        b = line
        stop = False

        for c in a:
            if c.isupper() and c not in b:
                print("NO")
                stop = True
                break

        if not stop:
            A = 0
            B = 0
            for c in a:
                if c.isupper():
                    A+=1
            for c in b:
                if c.isupper():
                    B+=1
            if A > B:
                print("NO")
                stop = True
        
        if not stop:
            l = 0
            a2 = a.upper()
            start = 0
            for c in b:
                i = start
                while i < len(a2):
                    if c == a2[i]:
                        l+=1
                        if i < len(a2) - 1:
                            start = i+1
                        break
                    i+=1

            for i in range(start+1, len(a)):
                if a[i].isupper():
                    print("NO")
                    break
            else:
                if l == len(b):
                    print("YES")
                else:
                    print("NO")

            a = None