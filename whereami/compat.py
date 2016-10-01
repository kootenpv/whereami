# whereami.predict
try:
    from sklearn.model_selection import cross_val_score
except ImportError:
    from sklearn.cross_validation import cross_val_score

# whereami.pipeline
try:
    FileNotFoundError = FileNotFoundError
except NameError:
    FileNotFoundError = IOError
