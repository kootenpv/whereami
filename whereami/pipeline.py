import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.cross_validation import train_test_split
from whereami.get_data import get_train_data
from whereami.utils import get_model_file


def cross_validate_model(pipeline, X, y, n=100):
    means = []
    for _ in range(n):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        pipeline.fit(X_train, y_train)
        means.append(np.mean(pipeline.predict(X_test) == y_test))
    return np.mean(means)


def train_model():
    model_file = get_model_file()
    X, y = get_train_data()
    # fantastic: because using "quality" rather than "rssi", we expect values 0-150
    # 0 essentially indicates no connection
    # 150 is something like best possible connection
    # Not observing a wifi will mean a value of 0, which is the perfect default.
    lp = make_pipeline(DictVectorizer(sparse=False),
                       RandomForestClassifier(n_estimators=100))
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp


def get_model():
    model_file = get_model_file()
    try:
        with open(model_file, "rb") as f:
            lp = pickle.load(f)
    except FileNotFoundError:
        msg = "First learn a location, e.g. with `metadate learn home 10`."
        raise FileNotFoundError(msg)
    return lp
