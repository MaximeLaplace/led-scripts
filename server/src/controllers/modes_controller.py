import inspect
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


def work(mode: str, segments_to_use: str, speed_factor: int = 1):
    strip = create_strip(segments_to_use)
    strip.reset()

    args = list(inspect.signature(modes[mode]).parameters.keys())
    args_values = list(inspect.signature(modes[mode]).parameters.values())
    for arg in args_values:
        if arg.default is arg.empty:
            args.pop(0)

    defaults = modes[mode].__defaults__

    if "wait_ms" in args:
        wait_ms_index = args.index("wait_ms")
        wait_ms = max(int(defaults[wait_ms_index] / speed_factor), 1)

        modes[mode](strip, wait_ms=wait_ms)
    else:
        modes[mode](strip)


def reload_modes_process(mode: str):
    globals_.current_mode = mode

    if globals_.modes_process.is_alive():
        globals_.modes_process.kill()

    globals_.modes_process = Process(
        target=work,
        args=(mode, globals_.segments_to_use, globals_.speed_factor),
    )
