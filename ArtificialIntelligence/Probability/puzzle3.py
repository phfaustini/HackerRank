# https://www.hackerrank.com/challenges/basic-probability-puzzles-3
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
    x.extend(['b']*3)
    
    y = ['r']*5
    y.extend(['b']*4)
    
    z = ['r']*4
    z.extend(['b']*4)
    
    outcome = {}
    
    numerator = 0
    denominator = 0
    for x_ball in x:
        for y_ball in y:
            for z_ball in z:
                denominator += 1
                
                outcome[x_ball] = 1
                
                if y_ball not in outcome:
                    outcome[y_ball] = 1
                else:
                    outcome[y_ball] += 1
                
                if z_ball not in outcome:
                    outcome[z_ball] = 1
                else:
                    outcome[z_ball] += 1                
                
                if 'r' in outcome and 'b' in outcome:
                    if outcome['r'] == 2 and outcome['b'] == 1:
                        numerator += 1
                
                outcome.clear()
                
    numerator, denominator = simplify_fraction(numerator, denominator)
    print(str(int(numerator))+"/"+str(int(denominator)))
