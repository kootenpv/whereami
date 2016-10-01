import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
from whereami.get_data import get_train_data
from whereami.utils import get_model_file
from whereami.compat import FileNotFoundError


def get_pipeline(clf=RandomForestClassifier(n_estimators=500, class_weight="balanced")):
    return make_pipeline(DictVectorizer(sparse=False),
                         clf)


def train_model():
    model_file = get_model_file()
    X, y = get_train_data()
    # fantastic: because using "quality" rather than "rssi", we expect values 0-150
    # 0 essentially indicates no connection
    # 150 is something like best possible connection
    # Not observing a wifi will mean a value of 0, which is the perfect default.
    lp = get_pipeline()
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
        msg = "First learn a location, e.g. with `whereami learn -l kitchen`."
        raise FileNotFoundError(msg)
    return lp
