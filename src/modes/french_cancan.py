import time

from rpi_ws281x import Color

from .utils.init_time import init_time
from .utils.rainbow import shift


def french_cancan(
    strip, wait_ms: int = 50, duration_s: int = 10, infinite: bool = True
):

    time_left = init_time(duration_s)

    colors_mod = [
        Color(0, 255, 0),
        Color(0, 0, 0),
        Color(125, 100, 125),
        Color(0, 0, 0),
        Color(255, 0, 0),
        Color(0, 0, 0),
    ]

    colors = [colors_mod[i % len(colors_mod)] for i in range(strip.numPixels())]

    while time_left() > 0 or infinite:
        strip.setArrayColor(colors)
        strip.show()
        time.sleep(wait_ms / 1000)
        shift(colors)
