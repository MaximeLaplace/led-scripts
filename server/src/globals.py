from multiprocessing import Process
from time import sleep

from scripts.src.startup_scripts.create_strip import UPPER_LED


def _do_nothing():
    while True:
        sleep(10)


def init():
    global segments_to_use
    global modes_process
    global current_mode
    global speed_factor

    segments_to_use = UPPER_LED
    current_mode = None
    speed_factor = 1

    modes_process = Process(target=_do_nothing)
