import random
import time

from .utils.array_address import address_array
from .utils.color_wheel import create_rainbow_array


def _bogo_controller(strip, wait_ms: int, duration_s: int):

    rainbow_array = create_rainbow_array(strip)
    iterations = int(duration_s * 1000 / wait_ms)

    for _ in range(iterations):
        address_array(strip, random.shuffle(rainbow_array))
        strip.show()
        time.sleep(wait_ms / 1000)


def bogo(strip, wait_ms: int = 50, durations_s: int = 10):
    """crée un arc-en-ciel et le mélange en bogo sort

    Args:
        wait_ms (int): temps d'attente entre chaque mélange en ms
        durations_s (int): temps total d'éxécution
    """
    _bogo_controller(strip, wait_ms=wait_ms, duration_s=durations_s)
