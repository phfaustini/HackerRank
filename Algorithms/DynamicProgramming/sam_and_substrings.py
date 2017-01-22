# https://www.hackerrank.com/challenges/sam-and-substrings

from fileinput import input

for numbers in input():
    numbers = [int(i) for i in numbers.rstrip()]
    total = 0
    for i in range (0, len(numbers)):
        aux = 0
        m=1
        for j in range(i, -1, -1):
            aux+=numbers[j]*m
            total += aux
            m*=10


    print(total)

'''    1 2 3 4
    
        1

        2
       12

        3
       23
      123

        4
       34
      234
     1234

        5
       45
      345
     2345
    12345'''