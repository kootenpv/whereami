import os
from whereami.pipeline import LocationPipeline
from whereami.get_data import get_train_data
from whereami.get_data import sample


def predict(tts=False):
    X, y = get_train_data()

    lp = LocationPipeline()
    lp.fit(X, y)

    if tts:
        pred = lp.predict(sample())[0]
        os.system("say " + pred + " &")
    else:
        print({x: y for x, y in zip(lp.clf.classes_, lp.predict_proba(sample())[0])})
