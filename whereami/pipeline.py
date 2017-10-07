import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
from whereami.get_data import get_train_data
from whereami.utils import get_model_file


class LearnLocation(Exception):
    pass


def get_pipeline(clf=RandomForestClassifier(n_estimators=100, class_weight="balanced")):
    return make_pipeline(DictVectorizer(sparse=False), clf)


def train_model(path=None):
    model_file = get_model_file(path)
    X, y = get_train_data(path)
    if len(X) == 0:
        raise ValueError("No wifi access points have been found during training")
    # fantastic: because using "quality" rather than "rssi", we expect values 0-150
    # 0 essentially indicates no connection
    # 150 is something like best possible connection
    # Not observing a wifi will mean a value of 0, which is the perfect default.
    lp = get_pipeline()
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp


def get_model(path=None):
    model_file = get_model_file(path)
    if not os.path.isfile(model_file):  # pragma: no cover
        msg = "First learn a location, e.g. with `whereami learn -l kitchen`."
        raise LearnLocation(msg)
    with open(model_file, "rb") as f:
        lp = pickle.load(f)
    return lp
