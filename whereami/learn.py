import subprocess
from tqdm import tqdm
import os

path = os.path.expanduser("~/.whereami")
if not os.path.exists(path):
    os.makedirs(path)


CMD = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s >> {}.txt"


def learn(label, n=100):
    cmd = CMD.format(os.path.join(path, label))
    for _ in tqdm(range(n)):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (out, _) = proc.communicate()
