# https://www.hackerrank.com/challenges/basic-probability-puzzles-2
# DONE

# For a single toss of 2 fair (evenly-weighted) dice, find the probability that the values rolled by 
# each die will be different and their sum is 6.

def probability(dice_size, value):
    p = 0
    for i in range(1, dice_size+1):
        for j in range(1, dice_size+1):
            if i+j == value and i != j:
                p+=1
    return p    


def simplify_fraction(numerator, denominator):
    mdc = 2
    denominator *= denominator
    while mdc <= min(numerator, denominator):
        if numerator % mdc == 0 and denominator % mdc == 0:
            numerator /=mdc
            denominator /=mdc
        else:
            mdc += 1
    return numerator, denominator


if __name__ == "__main__":
    import sys
    value = int(sys.argv[1]) # 6
    dice_size = int(sys.argv[2]) # 6
    p = probability(dice_size, value)
    p, d = simplify_fraction(p, dice_size)
    print(str(int(p))+"/"+str(int(d)))    