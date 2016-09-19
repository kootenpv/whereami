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

If you're adventurous and you want to learn to distinguish between couch #1 and couch #2 (i.e. 2 meters apart), it is the most robust when you switch locations and train in turn.

There's quite a lot of variation in WiFi, and if you train first 100 in location 1, then 100 in location 2, then predict on any space, location 2 will come out (due to changing signals over time). As more time passes, this "time variation" starts to play less of a role. But if you want immediate good results, train 20 on spot 1, then 20 on spot 2 and do this a couple of times.

Note that Couch vs Bedroom (~10 meters), is easier than 2 meters, and you should be able to train however you want.

### Almost entirely "copied" from:

https://github.com/schollz/find

That project used to be in Python, but is now written in Go. `whereami` is in Python with lessons learned implemented.
