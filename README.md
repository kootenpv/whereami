## whereami

Uses WiFi signals to predict where you are. Even works for small distances like 2-10 meters.

**OSX Only**

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
# {"bedroom": 0.99, "kitche": 0.01}
```
