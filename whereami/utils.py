import os


def get_whereami_path(path="~/.whereami"):
    return os.path.expanduser(path)


def ensure_whereami_path():
    path = get_whereami_path()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_model_file(path="~/.whereami", model="model.pkl"):
    return os.path.join(get_whereami_path(path), model)


def get_label_file(path, label):
    return os.path.join(get_whereami_path(path), label)
