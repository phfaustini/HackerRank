# https://www.hackerrank.com/challenges/craigslist-post-classifier-the-category/problem
# 71.847% acc offline
import json
from fileinput import input as ipt
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# TRAINING
N = None
X = []
y = []
for line in ipt("training.json"):
    if N is None:
        N = int(line.rstrip())
    else:
        line = line.rstrip()
        j = json.loads(line)
        y.append(j['category'])
        text = j['heading'] + " " + j["section"] + " " + j["city"]
        X.append(text)
tfidf = TfidfVectorizer(stop_words="english", binary=True, strip_accents="ascii")
X_transformed = tfidf.fit_transform(X)
clf = MultinomialNB()
clf.fit(X_transformed, y)

# TESTING
N = int(input())
X_test = []
while N > 0:
    j = json.loads(input().rstrip())
    X_test.append(j["heading"])
    N -= 1
X_test_transformed = tfidf.transform(X_test)
y_pred = clf.predict(X_test_transformed)
#for p in y_pred:
#    print(p)

y_true = []
for line in ipt("sample-test.out.json"):
    y_true.append(line.rstrip())

from sklearn.metrics import accuracy_score
print(accuracy_score(y_true, y_pred))