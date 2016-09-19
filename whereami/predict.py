from whereami.pipeline import LocationPipeline
from whereami.get_data import get_train_data
from whereami.get_data import sample


def get_model():
    # should really not have to train every time :-)
    # TODO: implement caching of model, retrain model after more learning
    X, y = get_train_data()
    lp = LocationPipeline()
    lp.fit(X, y)
    return lp


def predict_proba():
    lp = get_model()
    print({x: y for x, y in zip(lp.clf.classes_, lp.predict_proba(sample())[0])})


def predict(tts=False):
    print(lp.predict(sample())[0])
