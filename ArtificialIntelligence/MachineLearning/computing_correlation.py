#https://www.hackerrank.com/challenges/computing-the-correlation
# DONE

def pearson_correlation(l_seqX, l_seqY):
    """
        Given two lists of numbers, return their Pearson Correlation.
        Pearson Correlation is in interval of -1 to 1.
        1 is total positive linear correlation, 0 is no linear correlation, and −1 is total negative linear correlation.
        (As x increases, y also increases)                                 (This means that as x increases that y decreases)
        Source: http://www.statisticshowto.com/how-to-compute-pearsons-correlation-coefficients/

        Note: seqX, seqY must be lists of numbers of same size
    """
    from math import sqrt

    if not isinstance(l_seqX, list) or not isinstance(l_seqY, list):
        return -1

    if len(l_seqX) != len(l_seqY):
        return -2

    l_xy = []
    l_x2 = []
    l_y2 = []

    n = len(l_seqX)
    for i in range(0, n):
        l_xy.append(l_seqX[i] * l_seqY[i])
        l_x2.append(l_seqX[i] * l_seqX[i])
        l_y2.append(l_seqY[i] * l_seqY[i])

    sumXY = sum(l_xy)
    sumX2 = sum(l_x2)
    sumY2 = sum(l_y2)
    sumX = sum(l_seqX)
    sumY = sum(l_seqY)

    correlation = (n * sumXY - sumY * sumX) / sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY))

    return correlation


if __name__ == "__main__":
    maths = []
    physics = []
    chemistry = []

    rows = int(input())
    while rows:
        rows -= 1
        line = input()
        line = [int(i) for i in line.split("\t")]
        maths.append(line[0])
        physics.append(line[1])
        chemistry.append(line[2])

    # Mathematics and Physics, Physics and Chemistry, Mathematics and Chemistry
    mp = pearson_correlation(maths, physics)
    pc = pearson_correlation(physics, chemistry)
    mc = pearson_correlation(maths, chemistry)

    print("{:.2f}".format(mp))
    print("{:.2f}".format(pc))
    print("{:.2f}".format(mc))