import sys
from whereami.predict import predict
from whereami.predict import predict_proba
from whereami.learn import learn


def main():
    if "predict_proba" == sys.argv[1]:
        predict_proba()
    elif "predict" == sys.argv[1]:
        predict()
    elif "learn" in sys.argv[1] and len(sys.argv) == 4:
        category = sys.argv[2]
        n = int(sys.argv[3])
        learn(category, n)
