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


def work_factory(mode: str):
    def work():
        modes[mode](globals_.strip)

    return work


def work(mode: str):
    while True:
        modes[mode](globals_.strip)
        time.sleep(1)


def reload_modes_process(mode: str):
    print("reloading modes process")

    if globals_.modes_process.is_alive():
        print("killing modes process")
        globals_.modes_process.kill()
        globals_.strip.reset()

    globals_.modes_process = Process(target=work, args=(mode,))
