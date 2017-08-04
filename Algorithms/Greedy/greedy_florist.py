#https://www.hackerrank.com/challenges/greedy-florist
#DONE
from fileinput import input

n_flowers = k_customers = None

for line in input():
    line = [int(i) for i in line.rstrip().split(" ")]
    if n_flowers is None:
        n_flowers = line[0]
        k_customers = line[1]
    else:
        line = sorted(line)
        customers = [1]*k_customers
        i = 0
        price = 0
        while(len(line) > 0):
            flower = line.pop(-1)
            price += customers[i] * flower
            customers[i]+=1
            i = (i+1) % k_customers
        print(price)