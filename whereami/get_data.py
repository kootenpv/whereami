import json
import os
from access_points import get_scanner

from whereami.utils import ensure_whereami_path


def aps_to_dict(aps):
    return {ap['ssid'] + " " + ap['bssid']: ap['quality'] for ap in aps}


def sample():
    wifi_scanner = get_scanner()
    aps = wifi_scanner.get_access_points()
    return aps_to_dict(aps)


def get_train_data(folder=None):
    if folder is None:
        folder = ensure_whereami_path()
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
