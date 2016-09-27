from whereami.pipeline import get_pipeline
from whereami.pipeline import cross_validate_model
from whereami.get_data import aps_to_dict
from random import randint


def mock_get_train_data():
    X = [aps_to_dict([
        {"quality": randint(0, 130), "bssid": "XX:XX:XX:XX:XX:84", "ssid": "X", "security": "XX"},
        {"quality": randint(0, 130), "bssid": "XX:XX:XX:XX:XX:90",
         "ssid": "X", "security": "XX"},
        {"quality": randint(0, 130), "bssid": "XX:XX:XX:XX:XX:d1",
         "ssid": "X", "security": "XX"},
        {"quality": randint(0, 130), "bssid": "XX:XX:XX:XX:XX:c8", "ssid": "X", "security": "XX"}])
        for _ in range(10)]
    y = [0] * 5 + [1] * 5
    return X, y


def mock_get_model():
    return get_pipeline()


def test_train_model():
    X, y = mock_get_train_data()
    pipeline = mock_get_model()
    pipeline.fit(X, y)
    return pipeline, X, y


def test_crossval():
    X, y = mock_get_train_data()
    pipeline = mock_get_model()
    return cross_validate_model(pipeline, X, y, 5)


def test_predict():
    pipeline, X, y = test_train_model()
    assert pipeline.predict(X[0])[0] == y[0]
