import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def full_strobo(strip, wait_ms: int = 50, duration_s: int = 10, infinite: bool = True):

    time_left = init_time(duration_s)

    light = True
    while time_left() > 0 or infinite:
        for segment in strip.mode_segments:
            if light:
                segment.setColor(Color(125, 125, 125))
            else:
                strip.reset()
        strip.show()
        time.sleep(wait_ms / 1000)
        light = not light
