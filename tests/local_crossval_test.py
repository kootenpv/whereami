from whereami.predict import crossval


def test_crossval():
    crossval(folds=2, n=1)
