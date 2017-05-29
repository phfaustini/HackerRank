# https://www.hackerrank.com/challenges/stat-warmup
# DONE

def standard_deviation(l_seq):
    """
        It is a measure that is used to quantify the amount of variation or dispersion of a set of data values.
        A low standard deviation indicates that the data points tend to be close to the mean (also called the expected value) of the set.
        A high standard deviation indicates that the data points are spread out over a wider range of values.
    """
    from math import sqrt
    from math import fabs
    if not isinstance(l_seq, list):
        return -1

    mean = sum(l_seq) / len(l_seq)

    variance = 0
    for number in l_seq:
        variance += fabs(number - mean) * fabs(number - mean)
    variance /= len(l_seq)

    return sqrt(variance)


def mode(seq):
    """
        :param seq: a list of numbers
        :return: The element(s) which occurs most frequently. If many elements satisfy this criteria, returns the smallest one.
    """
    if not isinstance(seq, list):
        return -1

    occurrences = {}
    for number in seq:
        if number not in occurrences:
            occurrences[number] = 1
        else:
            occurrences[number] += 1

    biggest_value = 0
    biggest_keys = []
    for k, v in occurrences.items():
        if v > biggest_value:
            biggest_value = v
            biggest_keys.clear()
            biggest_keys.append(k)
        elif v == biggest_value:
            biggest_keys.append(k)

    biggest_keys = sorted(biggest_keys)
    return biggest_keys[0]


def median(seq):
    """
        :param seq: a list of numbers
        :return:  If the number of integers is odd, returns the middle element; else, the average of the middle two elements.
    """
    if not isinstance(seq, list):
        return -1

    seq = sorted(seq)
    size = len(seq)
    middle = int(size/2)  # truncates
    if size % 2 == 0: # even
        return (seq[middle] + seq[middle-1])/2
    else: # odd
        return seq[middle]


def confidence_interval_boundaries(seq, confidence_level=1.96):
    from math import  sqrt
    mean = sum(seq) / len(seq)
    standard_error_mean = standard_deviation(seq) / sqrt(len(seq))

    lower_boundary = mean - confidence_level * standard_error_mean
    upper_boundary = mean + confidence_level * standard_error_mean

    return (lower_boundary, upper_boundary)


if __name__ == "__main__":
    integers = int(input())
    numbers = input()
    numbers = [int(i) for i in numbers.split(" ")]

    mean = sum(numbers) / len(numbers)
    print("{:.1f}".format(mean))
    print("{:.1f}".format(median(numbers)))
    print(mode(numbers))
    print("{:.1f}".format(standard_deviation(numbers)))
    lower_boundary, upper_boundary = confidence_interval_boundaries(numbers)
    print("{:.1f}".format(lower_boundary), "{:.1f}".format(upper_boundary))