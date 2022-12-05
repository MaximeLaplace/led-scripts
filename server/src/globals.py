from multiprocessing import Process
from time import sleep

from scripts.src.startup_scripts.create_strip import create_strip


def do_nothing():
    while True:
        sleep(10)


def init():
    global strip
    global modes_process

    strip = create_strip("")
    modes_process = Process(target=do_nothing)
