import subprocess
import os
import json
from tqdm import tqdm
from whereami.get_data import sample


def ensure_whereami_path():
    path = os.path.expanduser("~/.whereami")
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def write_data(label_path, data, file_exists):
    with open(label_path, "a") as f:
        if file_exists:
            f.write("\n")
        f.write(json.dumps(data))


def learn(label, n=100):
    path = ensure_whereami_path()
    label_path = os.path.join(path, label + ".txt")
    file_exists = os.path.isfile(label_path)
    for _ in tqdm(range(n)):
        data = sample()
        write_data(label_path, data, file_exists)
        file_exists = True
