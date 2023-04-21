import time

from rpi_ws281x import Color

from ..utils.init_time import init_time
from ..utils.kanopeeUtils import map_letters, padForKanopeeCadre


def frigo(
    strip, wait_ms: int = 100, duration_s: int = 10, infinite: bool = True
):
    time_left = init_time(duration_s)

    color_array = [
        Color(255, 0, 0),
        Color(255, 0, 0),
        Color(255, 0, 128),
        Color(255, 0, 128),
        Color(255, 0, 255),
        Color(255, 0, 255),
        Color(0, 0, 255)
    ]

    off_color = Color(0, 0, 0)

    pattern = [
        [True, True, True, True, False, False, False],
        [False, False, False, True, True, True, True]
    ]

    while time_left() > 0 or infinite:
        for step in pattern:
            strip.setArrayColor(padForKanopeeCadre(map_letters(multiply(color_array, step, off_color))))
            strip.show()
            time.sleep(wait_ms / 1000)

def multiply(color_array, pattern, off_color):
    return [(color_array[i] if pattern[i] else off_color) for i in range(len(color_array))]