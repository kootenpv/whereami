import os

import json
from tqdm import tqdm
from whereami.get_data import sample
from whereami.pipeline import train_model
from whereami.utils import ensure_whereami_path
from whereami.utils import get_label_file


def write_data(label_path, data, file_exists):
    with open(label_path, "a") as f:
        if file_exists:
            f.write("\n")
        f.write(json.dumps(data))


def learn(label, n=100):
    path = ensure_whereami_path()
    label_path = get_label_file(path, label + ".txt")
    file_exists = os.path.isfile(label_path)
    for _ in tqdm(range(n)):
        try:
            data = sample()
            write_data(label_path, data, file_exists)
            file_exists = True
        except KeyboardInterrupt:
            break
    train_model()
