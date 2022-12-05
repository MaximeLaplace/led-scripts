import json

before = globals().copy()
from sr import *

after = globals().copy()

modes = {}
for key, value in after.items():
    if (
        key not in before.keys()
        and key != "before"
        and type(value).__name__ != "module"
    ):
        modes[key] = after[key]

modes = dict(sorted(modes.items(), key=lambda item: item[0]))
