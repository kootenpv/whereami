import os


def get_whereami_path(path="~/.whereami"):
    return os.path.expanduser(path)


def ensure_whereami_path():
    path = get_whereami_path()
    if not os.path.exists(path):  # pragma: no cover
        os.makedirs(path)
    return path


def get_model_file(path="~/.whereami", model="model.pkl"):
    return os.path.join(get_whereami_path(path), model)


def get_label_file(path, label):
    return os.path.join(get_whereami_path(path), label)


def rename_label(label, new_label, path="~/.whereami"):
    whereami_path = get_whereami_path(path)
    from_path = os.path.join(whereami_path, label + ".txt")
    new_path = os.path.join(whereami_path, new_label + ".txt")
    os.rename(from_path, new_path)
    print("Renamed {} to {}".format(from_path, new_path))
