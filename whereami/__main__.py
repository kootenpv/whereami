from whereami.predict import predict
from whereami.predict import predict_proba
from whereami.predict import crossval
from whereami.predict import locations
from whereami.learn import learn
from whereami.pipeline import train_model

from whereami import print_version
from whereami.utils import rename_label


def get_args_parser():
    import argparse
    from argparse import RawTextHelpFormatter
    desc = 'Uses WiFi signals and machine learning to predict where you are.'
    desc += '\nFeel free to try out commands, if anything is missing it will print help.'
    desc += '\n\nYou will want to start with `whereami learn`'
    p = argparse.ArgumentParser(description=desc, formatter_class=RawTextHelpFormatter)
    p.add_argument('--version', '-v', action='version', version=print_version())
    subparsers = p.add_subparsers(dest="command")

    predict_parser = subparsers.add_parser('predict')
    predict_parser.add_argument('--input_path', '-ip', default=None,
                                help='The directory containing current.loc.txt')
    predict_parser.add_argument('--model_path', '-mp', default=None,
                                help='The directory of the model / trained data')
    predict_parser.add_argument(
        '--device', '-d', default="", help='Change the wifi device to use')

    predict_proba_parser = subparsers.add_parser('predict_proba')
    predict_proba_parser.add_argument(
        '--input_path', '-ip', default=None, help='The directory containing current.loc.txt')
    predict_proba_parser.add_argument(
        '--model_path', '-mp', default=None, help='The directory of the model / trained data')
    predict_proba_parser.add_argument(
        '--device', '-d', default="", help='Change the wifi device to use')

    crossval_parser = subparsers.add_parser('crossval')
    crossval_parser.add_argument('--model_path', '-mp', default=None,
                                 help='The directory of the model / trained data')

    ls_parser = subparsers.add_parser('ls')
    ls_parser.add_argument('--model_path', '-mp', default=None,
                           help='The directory of the model / trained data')

    locations_parser = subparsers.add_parser('locations')
    locations_parser.add_argument('--model_path', '-mp', default=None,
                                  help='The directory of the model / trained data')

    learn_parser = subparsers.add_parser('learn')
    learn_parser.add_argument('--location', '-l', required=True,
                              help='A name-tag for location to learn.')
    learn_parser.add_argument('--device', '-d', default="",
                              help='Change the wifi device to use')
    learn_parser.add_argument('--num_samples', '-n', type=int,
                              default=1, help='Number of samples to take')

    rename = subparsers.add_parser('rename')

    rename.add_argument('--label', help='Label to rename')
    rename.add_argument('--new_label', help='New label name')
    rename.add_argument('--model_path', '-mp', default=None,
                        help='The directory of the model / trained data')

    train_parser = subparsers.add_parser('train')
    train_parser.add_argument('--model_path', '-mp', default=None,
                              help='The directory of the model / trained data')
    return p


def main():
    try:
        parser = get_args_parser()
        args = parser.parse_args()
        if args.command == "predict_proba":
            predict_proba(args.input_path, args.model_path, args.device)
        elif args.command == "predict":
            print(predict(args.input_path, args.model_path, args.device))
        elif args.command == "learn":
            learn(args.location, args.num_samples, args.device)
        elif args.command == "crossval":
            crossval(path=args.model_path)
        elif args.command in ["locations", "ls"]:
            locations(args.model_path)
        elif args.command == "rename":
            rename_label(args.label, args.new_label)
            print("Retraining model...")
            train_model()
        elif args.command == "train":
            train_model(args.model_path)
        else:
            parser.print_help()
            parser.exit(1)
    except (KeyboardInterrupt, SystemExit):
        exit()


if __name__ == '__main__':
    main()
