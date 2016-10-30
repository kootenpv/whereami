import sys
from whereami.__main__ import main


def test_main_learn():
    sys.argv[1:] = ["learn", "-l", "bed", "-n", "1"]
    main()


def test_main_predict():
    sys.argv[1:] = ["predict"]
    main()


def test_main_predict_proba():
    sys.argv[1:] = ["predict_proba"]
    main()


def test_main_locations():
    sys.argv[1:] = ["locations"]
    main()
