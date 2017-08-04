#https://www.hackerrank.com/challenges/travel-around-the-world
from fileinput import input

cities = None
fuel_capacity = None
get_fuel = []
cost = []


for line in input():
    line = line.rstrip().split(" ")
    if cities is None:
        cities = int(line[0])
        fuel_capacity = int(line[1])
    elif get_fuel == []:
        get_fuel = [int(i) for i in line]
    else:
        cost = [int(i) for i in line]
        output = 0

        viable = {} # city_index -> minFuelAllowedKnown
        unviable = {} # city_index -> maxFuelUnallowedKnown

        for i in range(0, cities):
            tank = 0
            stack = []
            start = i
            current = start
            left = cities
            while left > 0:
                tank += get_fuel[current]
                if tank > fuel_capacity: tank = fuel_capacity
                stack.append([current, tank])
                nextCity = current + 1 if current+1 < cities else 0

                if current in unviable:
                    if tank <= unviable[current]:
                        break

                if current in viable:
                    if tank >= viable[current]:
                        output += 1
                        break

                if tank - cost[nextCity] >= 0:
                    current = nextCity
                    left -= 1
                    tank -= cost[nextCity]
                    if left == 0:
                        while len(stack) > 0:
                            a = stack.pop()
                            viable[a[0]] = a[1]
                        output+=1
                else:
                    while len(stack) > 0:
                            a = stack.pop()
                            unviable[a[0]] = a[1]
                    break

        print(output)
