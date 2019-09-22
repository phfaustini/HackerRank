# https://www.hackerrank.com/challenges/temperature-predictions/problem

import pandas as pd
import numpy as np

N = int(input())
header = input()

tmaxl = []
tminl = []

#df = pd.DataFrame(columns=["year", "month", "tmax", "tmin"])
i = 0
while i < N:
    line = input().rstrip()
    line = line.split()
    year = int(line[0])
    month = line[1]
    tmin = float(line[2]) if not line[2].startswith("Missing") else np.nan
    tmax = float(line[3]) if not line[3].startswith("Missing") else np.nan
    tmaxl.append(tmax)
    tminl.append(tmin)
    #df.loc[i] = [year, month, tmin, tmax]
    i += 1

"""
def next_notnan(lst, index) -> float:
    if np.isnan(lst[index]):
        newIndex = index + 1 if index + 1 < len(lst) else 0
        return next_notnan(lst, newIndex)
    else: return lst[index]
def previous_notnan(lst, index) -> float:
    if np.isnan(lst[index]):
        newIndex = index - 1 if index - 1 >= 0 else len(lst) - 1
        return previous_notnan(lst, newIndex)
    else: return lst[index]

for i in range(N):
    if np.isnan(tmaxl[i]):
        tmaxl[i] = (next_notnan(tmaxl, i) + previous_notnan(tmaxl, i)) / 2
        print(tmaxl[i])
    if np.isnan(tminl[i]):
        tminl[i] = (next_notnan(tminl, i) + previous_notnan(tminl, i)) / 2
        print(tminl[i])
"""

series_max = pd.Series(tmaxl).interpolate()
series_min = pd.Series(tminl).interpolate()


for i in range(N):
    if np.isnan(tmaxl[i]):
        print(series_max[i])
    if np.isnan(tminl[i]):
        print(series_min[i])
