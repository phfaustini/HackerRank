# https://www.hackerrank.com/challenges/basic-probability-puzzles-4
# DONE


def simplify_fraction(numerator, denominator):
    mdc = 2
    while mdc <= min(numerator, denominator):
        if numerator % mdc == 0 and denominator % mdc == 0:
            numerator /=mdc
            denominator /=mdc
        else:
            mdc += 1
    return numerator, denominator


if __name__ == "__main__":
    x = ['r']*4
    x.extend(['b']*5)
    
    y = ['r']*3
    y.extend(['b']*7)
    
    outcome = {}
    
    numerator = 0
    denominator = 0
    for x_ball in x:
        for i in range(0, 10):
            for j in range(0, 10):
                if i != j:
                    denominator += 1
                    
                    outcome[x_ball] = 1
                        
                    if y[i] not in outcome:
                        outcome[y[i]] = 1
                    else:
                        outcome[y[i]] += 1 
                        
                    if y[j] not in outcome:
                        outcome[y[j]] = 1
                    else:
                        outcome[y[j]] += 1                     
                    
                    if 'r' in outcome and 'b' in outcome:
                        if outcome['b'] == 2 and outcome['r'] == 1:
                            numerator += 1
                    
                    outcome.clear()
                
    numerator, denominator = simplify_fraction(numerator, denominator)
    print(str(int(numerator))+"/"+str(int(denominator)))
