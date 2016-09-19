## whereami

Uses WiFi signals (and sklearn RandomForest) to predict where you are. Even works for small distances like 2-10 meters.

Your computer will known whether you are on Couch #1 or Couch #2.

**OSX Only (for now)**

### Installation

    pip install whereami

### Usage

```bash
    # in your bedroom, takes 100 samples
    whereami learn bedroom 100

    # in your kitchen, takes 100 samples
    whereami learn kitchen 100

    # text-to-speech where you are
    whereami predict -tts

    # numeric
    whereami predict
    # {"bedroom": 0.99, "kitchen": 0.01}
```

If you want to delete some of the last lines, or the data in general, visit your `$USER/.whereami` folder.

### Almost entirely "copied" from:

https://github.com/schollz/find

That project used to be in Python, but is now written in Go. `whereami` is in Python with lessons learned implemented.
