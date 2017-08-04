#https://www.hackerrank.com/challenges/pylons
from fileinput import input
n = k = None

def isCovered(cities, k, indexes):
    l = len(cities)
    for i in indexes:
        for j in range(0, k):
            if i+j < l: cities[i+j] = 1
            if i-j >= 0: cities[i-j] = 1
    if 0 not in cities:
        return True
    else:
        return False



for cities in input():
    cities = [int(i) for i in cities.rstrip().split(" ")]
    if n is None:
        n = cities[0]
        k = cities[1]
    else:
        stack = []
        generators = 0
        for i in cities:
            if i == 1:
                generators+=1
        minimum = generators
        for turnOff in range(1, generators+1):
            indexes = [-1]*turnOff
            for 
                copy = cities[:]
                if turnOff < minimum and isCovered(copy, k, ):
                    turnOff = minimum
                    break
        
        