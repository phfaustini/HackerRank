#https://www.hackerrank.com/challenges/bigger-is-greater
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
from fileinput import input
tests = None

for line in input():
    line = line.rstrip()
    if tests is None:
        tests = int(line)
    else:
        original = line
        line = [i for i in line]
        # Finding longest non increasing suffix
        pivot_index = 0
        for i in range(len(line)-1, 0, -1):
            if line[i-1] < line[i]:
                pivot_index = i-1
                break
        
        # Swapping pivot with the smallest number in the suffix, greater than the pivot
        for i in range(len(line)-1, 0, -1):
            if line[i] > line[pivot_index]:
                temp = line[i]
                line[i] = line[pivot_index]
                line[pivot_index] = temp
                break
        
        # Reversing suffix:
        prefix = line[0:pivot_index+1]
        suffix = line[pivot_index+1:]
        suffix.reverse()
        prefix.extend(suffix)
            
        new = ""
        for c in prefix:
            new+=c
        if new == original:
            print("no answer")
        else:
            print(new)
