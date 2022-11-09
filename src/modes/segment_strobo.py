import time

from rpi_ws281x import Color

from .utils.init_time import init_time
from .utils.reset_strip import reset_strip


def segment_strobo(
    strip,
    color: tuple[int, int, int] = (255, 255, 255),
    wait_ms: int = 50,
    duration_s: int = 10,
    infinite: bool = False,
):
    time_left = init_time(duration_s)

    index = 0
    length = len(strip.mode_segments)

    while time_left() > 0 or infinite:
        for i in range(length):
            strip.mode_segments[i].setColor(Color(0, 0, 0))
        strip.mode_segments[index % length].setColor(Color(*color))
        strip.show()
        index += 1
        time.sleep(wait_ms / 1000)

        reset_strip(strip)
        time.sleep(wait_ms / 1000)
