import random
import time

from rpi_ws281x import Color

from .utils.init_time import init_time
from .utils.reset_strip import reset_strip


def segment_strobo(
    strip, wait_ms: int = 50, duration_s: int = 10, infinite: bool = False
):
    time_left = init_time(duration_s)

    index = 0

    while time_left() > 0 or infinite:
        for i in range(8):
            strip.segments[i].setColor(Color(0, 0, 0))
        strip.segments[index % 8].setColor(Color(125, 125, 125))
        strip.show()
        index += 1
        time.sleep(wait_ms / 1000)

        reset_strip(strip)
        time.sleep(wait_ms / 1000)
