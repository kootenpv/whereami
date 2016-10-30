## whereami

[![Build Status](https://travis-ci.org/kootenpv/whereami.svg?branch=master)](https://travis-ci.org/kootenpv/whereami)
[![Coverage Status](https://coveralls.io/repos/github/kootenpv/whereami/badge.svg?branch=master)](https://coveralls.io/github/kootenpv/whereami?branch=master)
[![PyPI](https://img.shields.io/pypi/v/whereami.svg?style=flat-square)](https://pypi.python.org/pypi/whereami/)
[![PyPI](https://img.shields.io/pypi/pyversions/whereami.svg?style=flat-square)](https://pypi.python.org/pypi/whereami/)

Uses WiFi signals and machine learning (sklearn's RandomForest) to predict where you are. Even works for small distances like 2-10 meters.

Your computer will known whether you are on Couch #1 or Couch #2.

## Cross-platform

Works on OSX, Windows, Linux (tested on Ubuntu/Arch Linux).

The package [access_points](https://github.com/kootenpv/access_points) was created in the process to allow scanning wifi in a cross platform manner. Using `access_points` at command-line will allow you to scan wifi yourself and get JSON output.
`whereami` builds on top of it.

### Installation

    pip install whereami

### Usage

```bash
# in your bedroom, takes 100 samples
whereami learn -l bedroom -n 100

# in your kitchen, takes 100 samples
whereami learn -l kitchen -n 100

# get a list of already learned locations
whereami locations

# cross-validated accuracy on historic data
whereami crossval
# 0.99319

# use in other applications, e.g. by piping the most likely answer:
whereami predict | say
# Computer Voice says: "bedroom"

# probabilities per class
whereami predict_proba
# {"bedroom": 0.99, "kitchen": 0.01}
```

If you want to delete some of the last lines, or the data in general, visit your `$USER/.whereami` folder.

### Accuracy

Generally it should work really well. I've been able to learn using only 7 access points at home (test using `access_points -n`). At organizations you might see 70+.

Distance: anything around ~10 meters or more should get >99% accuracy.

If you're adventurous and you want to learn to distinguish between couch #1 and couch #2 (i.e. 2 meters apart), it is the most robust when you switch locations and train in turn. E.g. 20 in Spot A, then 20 in Spot B then start again with A.
Doing this in 100 in spot A, then 100 in spot B and then immediately using "predict" will yield spot B as an answer. No worries, the effect of this temporal overfitting disappears over time. And, in fact, this is only a real concern for the very short distances.

Height: Surprisingly, vertical difference in location is typically even more distinct than horizontal differences.

### Related Projects
- The [wherearehue](https://github.com/DeastinY/wherearehue) project can be used to toggle Hue light bulbs based on the learned locations.

### Common Issues

If the program fails with the error `nmcli-CRITICAL **: Error: Could not create NMClient object:` it is probably due to issues with the underlying [access_points](https://github.com/kootenpv/access_points) package. Check back there for further guidance before creating an issue here.

### Almost entirely "copied" from:

https://github.com/schollz/find

That project used to be in Python, but is now written in Go. `whereami` is in Python with lessons learned implemented.

### Tests

It's possible to locally run tests for python 2.7, 3.4 and 3.5 using tox.

    git clone https://github.com/kootenpv/whereami
    cd whereami
    python setup.py install
    tox
