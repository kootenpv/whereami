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


def learn(label, n=100):
    path = ensure_whereami_path()
    label_path = get_label_file(path, label + ".txt")
    for _ in tqdm(range(n)):
        try:
            new_sample = sample()
            if new_sample:
                write_data(label_path, new_sample)
        except KeyboardInterrupt:
            break
    train_model()
