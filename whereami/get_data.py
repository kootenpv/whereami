import json
import os
from access_points import get_scanner

from whereami.utils import ensure_whereami_path


def aps_to_dict(aps):
    return {ap['ssid'] + " " + ap['bssid']: ap['quality'] for ap in aps}


def sample():
    wifi_scanner = get_scanner()
    try:
        aps = wifi_scanner.get_access_points()
    except:
        aps = [{'bssid': '88:03:55:fc:61:41', 'security': 'WPA(PSK/TKIP/TKIP) WPA2(PSK/AES/TKIP) ', 'quality': 16, 'ssid': 'KPN-VGV7519FC6141'}, {'bssid': '4c:09:d4:38:74:84', 'security': 'WPA(PSK/TKIP/TKIP) WPA2(PSK/AES/TKIP) ', 'quality': 66, 'ssid': 'KPN-VGV7519387484'}, {'bssid': '5a:22:f8:df:16:91', 'security': 'NONE', 'quality': 36, 'ssid': 'KPN Fon'}, {'bssid': '54:22:f8:df:16:90', 'security': 'WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP) ', 'quality': 36, 'ssid': 'H368NDF1690'}, {
            'bssid': '00:23:cd:19:3a:d1', 'security': 'WPA(PSK/TKIP/TKIP) ', 'quality': 88, 'ssid': 'KalkZeist'}, {'bssid': '6c:aa:b3:66:d3:68', 'security': 'WPA2(802.1x/AES/AES) ', 'quality': 30, 'ssid': 'Ziggo'}, {'bssid': '6c:aa:b3:26:d3:68', 'security': 'NONE', 'quality': 24, 'ssid': 'Free Wi-Fi Zeist'}, {'bssid': '18:83:bf:03:45:8f', 'security': 'WPA2(PSK/AES/AES) ', 'quality': 24, 'ssid': 'VGV751903458F'}, {'bssid': 'b4:82:fe:19:d0:c8', 'security': 'WPA(PSK/TKIP/TKIP) WPA2(PSK/AES/TKIP) ', 'quality': 88, 'ssid': 'Thomson19D0C8'}]
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
