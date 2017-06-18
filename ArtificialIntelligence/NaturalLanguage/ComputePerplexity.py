# https://www.hackerrank.com/challenges/nlp-compute-the-perplexity
# DONE

# In information theory, perplexity is a measurement of how well a probability distribution or probability model predicts a sample. 
# It may be used to compare probability models. A low perplexity indicates the probability distribution is good at predicting the sample.

def Perplexity(cross_entropy):
    return 2**cross_entropy
    

if __name__ == "__main__":
    from sys import argv
    cross_entropy = 9.91
    if len(argv) > 1:
        cross_entropy = int(argv[1])
    print("{:.2f}".format(Perplexity(cross_entropy)))
    
    