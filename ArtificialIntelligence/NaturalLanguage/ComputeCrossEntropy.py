# https://www.hackerrank.com/challenges/nlp-compute-the-cross-entropy

def CrossEntropy(cross_entropy):
    from math import log2
    return log2(cross_entropy)
    

if __name__ == "__main__":
    from sys import argv
    perplexity = 170
    if len(argv) > 1:
        perplexity = int(argv[1])
    print("{:.2f}".format(CrossEntropy(perplexity)))