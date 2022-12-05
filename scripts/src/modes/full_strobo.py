import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def full_strobo(strip, wait_ms: int = 100, duration_s: int = 10, infinite: bool = True):

    time_left = init_time(duration_s)

    light = True
    offset = 0
    while time_left() > 0 or infinite:
        if light:
            for segment in strip.mode_segments:
                for l in range(offset, segment.numPixels(), 2):
                    segment.setPixelColor(l, Color(125, 125, 125))
        else:
            strip.reset()
            offset = offset * -1 + 1
        strip.show()
        time.sleep(wait_ms / 1000)
        light = not light
