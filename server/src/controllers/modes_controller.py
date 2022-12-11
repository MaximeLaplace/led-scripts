import time
from multiprocessing import Process

import server.src.globals as globals_
from scripts.src.startup_scripts.create_strip import create_strip

before = globals().copy()
from scripts.src.modes import *

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


def work(mode: str, segments_to_use: str):
    strip = create_strip(segments_to_use)
    strip.reset()
    while True:
        modes[mode](strip)
        time.sleep(1)


def reload_modes_process(mode: str):
    globals_.current_mode = mode

    if globals_.modes_process.is_alive():
        globals_.modes_process.kill()
        # globals_.strip.reset()

    globals_.modes_process = Process(
        target=work,
        args=(
            mode,
            globals_.segments_to_use,
        ),
    )
