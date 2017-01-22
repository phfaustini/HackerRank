#https://www.hackerrank.com/challenges/fibonacci-modified?h_r=internal-search
from fileinput import input

def fib(t1, t2):
    return t1 + t2*t2

for line in input():
    line = line.rstrip()
    line = [int(i) for i in line.split(" ")]
    t1 = line[0]
    t2 = line[1]
    tn = line[2] - 2
    
    temp = None
    
    while tn > 0:
        temp = fib(t1, t2)
        t1 = t2
        t2 = temp
        tn-=1
    
    print(temp)
