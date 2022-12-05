import time
from multiprocessing import Process

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


def do_nothing():
    while True:
        time.sleep(1)


modes_process = Process(target=do_nothing)

strip = create_strip("")


def work_factory(mode: str):
    def work():
        print("bonjour working")
        modes[mode](strip)

    return work


def reload_modes_process(mode: str):
    global modes_process

    if modes_process.is_alive():
        modes_process.kill()
        strip.reset()

    modes_process = Process(target=work_factory(mode))
