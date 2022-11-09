import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def lamp(
    strip,
    color: tuple[int, int, int] = (50, 10, 50),
    duration_s: int = 10,
    infinite: bool = True,
):
    time_left = init_time(duration_s)

    while time_left() > 0 or infinite:
        strip.setColor(Color(*color))
        strip.show()
        time.sleep(duration_s)
