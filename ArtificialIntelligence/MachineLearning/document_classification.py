#https://www.hackerrank.com/challenges/document-classification/problem
# 63.62% 

from fileinput import input as inpt

from sklearn.feature_extraction.text import TfidfVectorizer #  Equivalent to CountVectorizer followed by TfidfTransformer.
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np


f = "trainingdata.txt"

number_documents = None

texts = []
y_training = []
X_training = []

# load training data to memory
for line in inpt(f):
    if number_documents is None:
        number_documents = int(line)
    elif len(line) > 1:
        y_training.append(int(line[0]))
        texts.append(line[2:])


text_clf = Pipeline(
            [('vecttfidf', TfidfVectorizer(max_features=800, stop_words='english')),
             ('clf', MultinomialNB())])

text_clf.fit(texts, np.array(y_training))

X_test = []
documents = int(input())
while documents:
    documents -= 1
    X_test.append(str(input()))

pred = text_clf.predict(X_test)
for p in pred:
    print(p)
