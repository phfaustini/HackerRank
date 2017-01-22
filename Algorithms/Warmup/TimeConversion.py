#!/bin/python3

import sys


time = input().strip()
time = time.split(":")
if("P" in time[2]):
    time[0] = 12+int(time[0])
    if time[0] == 24: 
        time[0] = "12"
    elif time[0] < 10:
        time[0] = "0"+str(time[0])
    else:
        time[0] = str(time[0])
else:
    if time[0] == "12": time[0] = "00"
time[2] = time[2][0:2]
print(time[0], time[1], time[2], sep=":")
