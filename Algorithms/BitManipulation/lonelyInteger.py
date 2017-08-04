#https://www.hackerrank.com/challenges/lonely-integer
# DONE
#!/usr/bin/py
# Head ends here
def lonelyinteger(b):
    answer = 0
    d = {}

    for i in b:
        if i not in d:
            d[i] = 1
            answer = i
        else:
            d[i]+=1
    
    for k, v in d.items():
        if v == 1:
            answer = k

    return answer

# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
