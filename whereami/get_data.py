import json
import subprocess
import os
from access_points import get_scanner


def sample():
    wifi_scanner = get_scanner()
    aps = wifi_scanner.get_access_points()
    dc = {}
    for ap in aps:
        key = ap['ssid'] + " " + ap['bssid']
        value = ap['quality']
        dc[key] = value
    return dc


def get_train_data(folder=None):
    if folder is None:
        folder = os.path.expanduser("~/.whereami")
    X = []
    y = []
    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            data = []
            with open(os.path.join(folder, fname)) as f:
                for line in f:
                    data.append(json.loads(line))
            X.extend(data)
            y.extend([fname.rstrip(".txt")] * len(data))
    return X, y
