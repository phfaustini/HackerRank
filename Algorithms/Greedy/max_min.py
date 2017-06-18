# https://www.hackerrank.com/challenges/angry-children/problem
# DONE

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    numbers = []
    while n > 0:
        n -= 1
        numbers.append(int(input()))
    numbers = sorted(numbers)
    size = len(numbers)
    unfairness = numbers[-1]
    
    for i in range((size-(k-1))):
        if numbers[i + (k-1)] - numbers[i] < unfairness:
            unfairness = numbers[i + (k-1)] - numbers[i]
    print(unfairness)