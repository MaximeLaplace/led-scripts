import time

from rpi_ws281x import Color

from ..utils.init_time import init_time
from ..utils.rainbow import shift
from ..utils.kanopeeUtils import map_letters, padForKanopeeCadre


def one_by_one(
    strip, color=(255, 255, 255), wait_ms: int = 469, duration_s: int = 10, infinite: bool = True
):
    time_left = init_time(duration_s)

    colors = [
        Color(*color),
        Color(0, 0, 0),
        Color(0, 0, 0),
        Color(0, 0, 0),
        Color(0, 0, 0),
        Color(0, 0, 0),
        Color(0, 0, 0)
    ]

    while time_left() > 0 or infinite:
        strip.setArrayColor(padForKanopeeCadre(map_letters(list(reversed(colors)))))
        strip.show()
        time.sleep(wait_ms / 1000)
        shift(colors)
