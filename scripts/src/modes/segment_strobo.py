import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def segment_strobo(
    strip,
    color: tuple[int, int, int] = (255, 255, 255),
    wait_ms: int = 50,
    duration_s: int = 10,
    infinite: bool = True,
):
    time_left = init_time(duration_s)

    index = 0
    length = len(strip.mode_segments)
    print(strip.mode_segments)

    while time_left() > 0 or infinite:
        for i in range(length):
            strip.mode_segments[i].setColor(Color(0, 0, 0))
        strip.mode_segments[index % length].setColor(Color(*color))
        strip.show()
        index += 1
        time.sleep(wait_ms / 1000)

        strip.reset()
        time.sleep(wait_ms / 1000)
