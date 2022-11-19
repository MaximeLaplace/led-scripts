import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def full_strobo(strip, wait_ms: int = 100, duration_s: int = 10, infinite: bool = True):

    time_left = init_time(duration_s)

    light = True
    while time_left() > 0 or infinite:
        for segment in strip.mode_segments:
            if light:
                for l in range(0, segment.numPixels(), 2):
                    segment.setPixelColor(l, Color(125, 125, 125))
            else:
                strip.reset()
        strip.show()
        time.sleep(wait_ms / 1000)
        light = not light
