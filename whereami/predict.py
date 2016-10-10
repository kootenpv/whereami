from collections import Counter

from whereami.get_data import get_train_data
from whereami.get_data import sample
from whereami.pipeline import get_model
from whereami.compat import cross_val_score


def predict_proba():
    lp = get_model()
    print({x: y for x, y in zip(lp.classes_, lp.predict_proba(sample())[0])})


def predict():
    lp = get_model()
    print(lp.predict(sample())[0])


def crossval(clf=None, X=None, y=None, folds=10, n=5):
    if X is None or y is None:
        X, y = get_train_data()
    clf = clf or get_model()
    tot = 0
    print("KFold folds={}, running {} times".format(folds, n))
    for i in range(n):
        res = cross_val_score(clf, X, y, cv=10).mean()
        tot += res
        print("{}/{}: {}".format(i + 1, n, res))
    print("-------- total --------")
    print(tot / n)
    return tot / n

def locations():
    X, y = get_train_data()
    if len(y) == 0:
        msg = "No location samples available. First learn a location, e.g. with `whereami learn -l kitchen`."
        print(msg)
    else:
        occurrences = Counter(y)
        for key,value in occurrences.items():
            print("{}: {}".format(key,value))
