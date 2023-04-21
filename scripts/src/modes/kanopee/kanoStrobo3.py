import time

from rpi_ws281x import Color

from ..utils.init_time import init_time
from ..utils.kanopeeUtils import invert


def kano_strobo3(
    strip, color=(255, 255, 255), wait_ms: int = 100, duration_s: int = 10, infinite: bool = True
):
    on_color = Color(*color)
    off_color = Color(0, 0, 0)
    time_left = init_time(duration_s)
    length = len(strip.mode_segments)

    steps = [
        (off_color, on_color),
        (off_color, off_color),
        (on_color, off_color),
        (off_color, off_color)
    ]

    while time_left() > 0 or infinite:
        for color1, color2 in steps:
            for i in range(3):
                strip.mode_segments[i].setColor(color1)
            for i in range(3, length):
                strip.mode_segments[i].setColor(color2)
            strip.show()
            time.sleep(wait_ms / 1000)
