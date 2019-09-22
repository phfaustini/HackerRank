# https://www.hackerrank.com/challenges/stack-exchange-question-classifier/problem
# DONE (87% score)
from fileinput import input
import json

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

N = None

X = []
y = []

# TRAINING
for line in input("training.json"):
    if N is None:
        N = int(line.rstrip())
    else:
        line = line.rstrip()
        j = json.loads(line)
        y.append(j['topic'])
        text = j['excerpt'] + " " + j['question']
        X.append(text)

tfidf = TfidfVectorizer()
X_transformed = tfidf.fit_transform(X)

clf = MultinomialNB()
clf.fit(X_transformed, y)

# TESTING
X_test = []
N = None
for line in input():
    if N is None:
        N = int(line.rstrip())
    else:
        line = line.rstrip()
        j = json.loads(line)
        text = j['excerpt'] + " " + j['question']
        X_test.append(text)

X_test_transformed = tfidf.transform(X_test)
y_pred = clf.predict(X_test_transformed)
for prediction in y_pred:
    print(prediction)
