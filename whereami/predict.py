from collections import Counter

from whereami.compat import cross_val_score
from whereami.get_data import get_train_data, get_external_sample
from whereami.get_data import sample
from whereami.pipeline import get_model


def predict_proba(input_path=None, model_path=None):
    lp = get_model(model_path)
    data_sample = sample() if input_path is None else get_external_sample(input_path)
    print(
        {x: y for x, y in
         zip(lp.classes_, lp.predict_proba(data_sample)[0])})


def predict(input_path=None, model_path=None):
    lp = get_model(model_path)
    data_sample = sample() if input_path is None else get_external_sample(input_path)
    return lp.predict(data_sample)[0]


def crossval(clf=None, X=None, y=None, folds=10, n=5, path=None):
    if X is None or y is None:
        X, y = get_train_data(path)
    clf = clf or get_model(path)
    tot = 0
    print("KFold folds={}, running {} times".format(folds, n))
    for i in range(n):
        res = cross_val_score(clf, X, y, cv=folds).mean()
        tot += res
        print("{}/{}: {}".format(i + 1, n, res))
    print("-------- total --------")
    print(tot / n)
    return tot / n


def locations(path=None):
    X, y = get_train_data(path)
    if len(y) == 0:  # pragma: no cover
        msg = "No location samples available. First learn a location, e.g. with `whereami learn -l kitchen`."
        print(msg)
    else:
        occurrences = Counter(y)
        for key, value in occurrences.items():
            print("{}: {}".format(key, value))
