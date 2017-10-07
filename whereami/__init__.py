import sys

__project__ = "whereami"
__version__ = "0.4.70"
__repo__ = "https://github.com/kootenpv/whereami"

from whereami.learn import learn
from whereami.pipeline import get_pipeline
from whereami.predict import predict, predict_proba, crossval, locations


def print_version():
    sv = sys.version_info
    py_version = "{}.{}.{}".format(sv.major, sv.minor, sv.micro)
    version_parts = __version__.split(".")
    s = "{} version: [{}], Python {}".format(__project__, __version__, py_version)
    s += "\nMajor version: {}  (breaking changes)".format(version_parts[0])
    s += "\nMinor version: {}  (extra feature)".format(version_parts[1])
    s += "\nMicro version: {} (commit count)".format(version_parts[2])
    s += "\nFind out the most recent version at {}".format(__repo__)
    return s
