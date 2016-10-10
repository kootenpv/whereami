from whereami.predict import predict
from whereami.predict import predict_proba
from whereami.predict import crossval
from whereami.predict import locations
from whereami.learn import learn

from whereami import print_version


def get_args_parser():
    import argparse
    from argparse import RawTextHelpFormatter
    desc = 'Uses WiFi signals and machine learning to predict where you are.'
    desc += '\nFeel free to try out commands, if anything is missing it will print help.'
    desc += '\n\nYou will want to start with `whereami learn`'
    p = argparse.ArgumentParser(description=desc, formatter_class=RawTextHelpFormatter)
    p.add_argument('--version', '-v', action='version', version=print_version())
    subparsers = p.add_subparsers(dest="command")
    subparsers.add_parser('predict')
    subparsers.add_parser('predict_proba')
    subparsers.add_parser('crossval')
    subparsers.add_parser('locations')
    learn_parser = subparsers.add_parser('learn')
    learn_parser.add_argument('--location', '-l', required=True,
                              help='A name-tag for location to learn.')
    learn_parser.add_argument('--num_samples', '-n', type=int, default=100,
                              help='Number of samples to take')
    return p


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    if args.command == "predict_proba":
        predict_proba()
    elif args.command == "predict":
        predict()
    elif args.command == "learn":
        learn(args.location, args.num_samples)
    elif args.command == "crossval":
        crossval()
    elif args.command == "locations":
        locations()
    else:
        parser.print_help()
        parser.exit(1)
