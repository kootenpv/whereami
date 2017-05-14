import time
import json

from tqdm import tqdm

from whereami.get_data import sample

from whereami.pipeline import train_model
from whereami.utils import ensure_whereami_path
from whereami.utils import get_label_file


def write_data(label_path, data):
    with open(label_path, "a") as f:
        f.write(json.dumps(data))
        f.write("\n")


def learn(label, n=20, device=""):
    path = ensure_whereami_path()
    label_path = get_label_file(path, label + ".txt")
    for i in tqdm(range(n)):
        if i != 0:
            time.sleep(15)
        try:
            new_sample = sample(device)
            if new_sample:
                write_data(label_path, new_sample)
        except KeyboardInterrupt:  # pragma: no cover
            break
    train_model()
