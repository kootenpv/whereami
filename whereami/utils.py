import os


def get_whereami_path(path=None):
    if path is None:
        _USERNAME = os.getenv("SUDO_USER") or os.getenv("USER") or "/"
        path = os.path.expanduser('~' + _USERNAME)
        path = os.path.join(path, ".whereami")
    return os.path.expanduser(path)


def ensure_whereami_path():
    path = get_whereami_path()
    if not os.path.exists(path):  # pragma: no cover
        os.makedirs(path)
    return path


def get_model_file(path=None, model="model.pkl"):
    path = ensure_whereami_path() if path is None else path
    return os.path.join(path, model)


def get_label_file(path, label):
    return os.path.join(get_whereami_path(path), label)


def rename_label(label, new_label, path=None):
    path = ensure_whereami_path() if path is None else path
    from_path = os.path.join(path, label + ".txt")
    new_path = os.path.join(path, new_label + ".txt")
    os.rename(from_path, new_path)
    print("Renamed {} to {}".format(from_path, new_path))
