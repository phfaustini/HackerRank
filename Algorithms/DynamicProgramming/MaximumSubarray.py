# https://www.hackerrank.com/challenges/maxsubarray

def MaximumSubArraySum(array):
    
    sequence = array.pop(0)
    
    while len(array) > 0:
        v = array.pop(0)
        if sequence + v > 0:
            sequence+=v
        else:
            sequence = 0
        
        
        
    return sequence
        

            
            

if __name__ == "__main__":
    tests = int(input())
    while tests > 0:
        tests -= 1
        size = int(input())
        array = [int(i) for i in input().split()]
        print(MaximumSubArraySum(array))
        
        