#!/bin/python3
#https://www.hackerrank.com/challenges/the-time-in-words
# DONE
import sys

h = int(input().strip())
m = int(input().strip())

d = {}
d[0] = "o' clock"
d[1] = "one"
d[2] = "two"
d[3] = "three"
d[4] = "four"
d[5] = "five"
d[6] = "six"
d[7] = "seven"
d[8] = "eight"
d[9] = "nine"
d[10] = "ten"
d[11] = "eleven"
d[12] = "twelve"
d[13] = "thirteen"
d[14] = "fourteen"
d[16] = "sixteen"
d[17] = "seventeen"
d[18] = "eightenn"
d[19] = "nineteen"
d[20] = "twenty"
d[30] = "thirty"
d[40] = "fourty"
d[50] = "fifty"

if m == 0:
    print(d[h]+" "+d[m])
elif m == 1:
    print(d[m]+" minute past "+d[h])
elif m == 30:
    print("half past "+d[h])
elif m == 45:
    print("quarter to "+d[h+1])
elif m == 15:
    print("quarter past "+d[h])
elif m <=20:
    print(d[m]+" minutes past "+d[h])
elif m < 30:
    bm = m // 10
    sm = m % 10
    bm *= 10
    print(d[bm]+" "+d[sm]+" minutes past "+d[h])
elif m > 30:
    m = 60 - m
    h += 1
    if m == 1:
        print(d[m]+" minute to "+d[h])
    elif m <= 20:
        print(d[m]+" minutes to "+d[h])
    else:
        bm = m // 10
        sm = m % 10
        bm *= 10
        print(d[bm]+" "+d[sm]+" minutes to "+d[h])