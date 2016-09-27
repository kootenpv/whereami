import json
import subprocess
import os
from access_points import get_scanner

from whereami.utils import ensure_whereami_path


def sample():
    wifi_scanner = get_scanner()
    aps = wifi_scanner.get_access_points()
    return {ap['ssid'] + " " + ap['bssid']: ap['quality'] for ap in aps}

def get_train_data(folder=None):
    if folder is None:
        folder = ensure_whereami_path()
    X = []
    y = []
    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            with open(os.path.join(folder, fname)) as f:
                data = map(json.loads, f)
            X.extend(data)
            y.extend(fname.rstrip(".txt") for _ in data)
    return X, y
