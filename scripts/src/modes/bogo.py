import random
import time

from .utils.init_time import init_time
from .utils.rainbow import create_rainbow_array


def _bogo_controller(
    strip,
    wait_ms: int = 100,
    duration_s: int = 10,
    infinite: bool = True,
):
    time_left = init_time(duration_s)
    rainbow_array = create_rainbow_array(strip)

    while infinite or time_left() > 0:
        random.shuffle(rainbow_array)
        strip.setArrayColor(rainbow_array)
        strip.show()
        time.sleep(wait_ms / 1000)


def bogo(
    strip,
    wait_ms: int = 100,
    durations_s: int = 10,
    infinite: bool = True,
):
    """crée un arc-en-ciel et le mélange en bogo sort

    Args:
        wait_ms (int): temps d'attente entre chaque mélange en ms
        durations_s (int): temps total d'éxécution
    """
    _bogo_controller(
        strip,
        wait_ms=wait_ms,
        duration_s=durations_s,
        infinite=infinite,
    )
