# https://www.hackerrank.com/challenges/maxsubarray

def MaximumSubArraySum(array, size):
    maximum = array[0]
    
    if size == 1:
        return maximum
    
    subarray_sums = []
    for i in range(size):
        subarray_sums.append([])
        for j in range(size):
            subarray_sums[i].append(0)            
    
    currentSum = 0
    for i in range(size):
        currentSum += array[i]
        subarray_sums[0][i] = currentSum
        subarray_sums[i][i] = array[i]
        maximum = max(maximum, max(currentSum, array[i]))   
        
    for i in range(1, size):
        for j in range(i+1, size):
            if i != j:
                subarray_sums[i][j] = subarray_sums[0][j] - subarray_sums[0][i-1]
                maximum = max(maximum, subarray_sums[i][j])
        
    return maximum            
            

if __name__ == "__main__":
    tests = int(input())
    while tests > 0:
        tests -= 1
        size = int(input())
        array = [int(i) for i in input().split()]
        contiguous = MaximumSubArraySum(array, size)
        
        maximum = non_contiguous = array[0]
        for v in array[1:]:
            if v > 0:
                non_contiguous += v 
            if v > maximum:
                maximum = v
        non_contiguous = max(non_contiguous, maximum)
            
        print(str(contiguous)+" "+str(non_contiguous))
