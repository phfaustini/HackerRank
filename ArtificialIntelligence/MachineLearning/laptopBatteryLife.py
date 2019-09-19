#!/bin/python3

"""
# Visualising data before:
import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt("trainingdata.txt", delimiter=',', encoding='utf-8')
X = data[:,0]
y = data[:,1]
xs, ys = zip(*sorted(zip(X, y)))
plt.plot(xs, ys)
plt.show()

"""


if __name__ == '__main__':
    timeCharged = float(input())
    if timeCharged >= 4:
        print(8.00, end="")
    else:
        print(timeCharged*2)
