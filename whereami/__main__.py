import sys
from whereami.predict import predict
from whereami.learn import learn


def main():
    if "predict" == sys.argv[1]:
        predict("-tts" in sys.argv)
    elif "learn" in sys.argv[1] and len(sys.argv) == 4:
        category = sys.argv[2]
        n = int(sys.argv[3])
        learn(category, n)
