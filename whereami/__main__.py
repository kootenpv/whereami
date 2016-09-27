from whereami.predict import predict
from whereami.predict import predict_proba
from whereami.predict import crossval
from whereami.learn import learn


def get_args_parser():
    import argparse
    desc = 'Uses WiFi signals and machine learning to predict where you are.'
    p = argparse.ArgumentParser(description=desc)
    subparsers = p.add_subparsers(dest="command")
    subparsers.add_parser('predict')
    subparsers.add_parser('predict_proba')
    subparsers.add_parser('crossval')
    learn_parser = subparsers.add_parser('learn')
    learn_parser.add_argument('--location', '-l', required=True,
                              help='A name-tag for location to learn.')
    learn_parser.add_argument('--num_samples', '-n', type=int, default=100,
                              help='Number of samples to take')
    return p


def main():
    args = get_args_parser().parse_args()
    if args.command == "predict_proba":
        predict_proba()
    elif args.command == "predict":
        predict()
    elif args.command == "learn":
        learn(args.location, args.num_samples)
    elif args.command == "crossval":
        crossval()
