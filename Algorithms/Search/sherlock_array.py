#https://www.hackerrank.com/challenges/sherlock-and-array
# DONE
from fileinput import input

tests = None
size = None
for line in input():
    line = line.rstrip()
    if tests is None:
        tests = int(line)
    elif size is None:
        size = int(line)
    else:
        if size == 2:
            print("NO")
        elif size == 1:
            print("YES")
        else:
            line = [int(i) for i in line.split(" ")]
            left = line[0]
            right = sum(line[2:])

            for i in range(1, size-1):
                if left == right:
                    print("YES")
                    break
                else:
                    left += line[i]
                    right -= line[i+1]
            else:
                print("NO")
        size = None