from whereami.get_data import get_train_data
from whereami.get_data import sample
from whereami.pipeline import get_model
from whereami.pipeline import cross_validate_model


def predict_proba():
    lp = get_model()
    print({x: y for x, y in zip(lp.classes_, lp.predict_proba(sample())[0])})


def predict():
    lp = get_model()
    print(lp.predict(sample())[0])


def crossval():
    X, y = get_train_data()
    lp = get_model()
    print(cross_validate_model(lp, X, y))
