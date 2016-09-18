import subprocess
import os


def get_parser(line):
    bbsid = line.index("BSSID")
    rssi = line.index("RSSI")
    channel = line.index("CHANNEL")
    security = line.index("SECURITY")
    return [("SSID", (0, bbsid)),
            ("BSSID", (bbsid, rssi)),
            ("RSSI", (rssi, channel)),
            ("SECURITY", (security, -1))]


def sample():
    cmd = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s"
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()
    dc = {}
    parser = None
    for line in out.decode("utf8").split("\n"):
        if line.strip().startswith("SSID"):
            parser = get_parser(line)
        elif line:
            row = [line[inds[0]:inds[1]].strip() for name, inds in parser]
            key = row[0] + " " + row[1]
            value = int(row[2])
            dc[key] = value
    return dc


def get_train_data(folder=None):
    if folder is None:
        folder = os.path.expanduser("~/.whereami")
    parser = None
    X = []
    y = []
    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            data = []
            with open(os.path.join(folder, fname)) as f:
                case = {}
                for line in f:
                    if line.strip().startswith("SSID"):
                        if parser is None:
                            parser = get_parser(line)
                        else:
                            data.append(case)
                        case = {}
                    elif line:
                        row = [line[inds[0]:inds[1]].strip() for name, inds in parser]
                        key, value = row[0] + " " + row[1], int(row[2])
                        case[key] = value
                data.append(case)
            X.extend(data)
            y.extend([fname.rstrip(".txt")] * len(data))
    return X, y
