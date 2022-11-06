import random
import time

from .utils.address_led_with_array import address_led_with_array
from .utils.color_wheel import create_rainbow_array


def _bogo_controller(strip, wait_ms: int, duration_s: int, chance_of_light: int):

    rainbow_array = create_rainbow_array(strip)
    iterations = int(duration_s * 1000 / wait_ms)

    for _ in range(iterations):
        random.shuffle(rainbow_array)
        address_led_with_array(strip, rainbow_array, chance_of_light=chance_of_light)
        strip.show()
        time.sleep(wait_ms / 1000)


def bogo(strip, wait_ms: int = 50, durations_s: int = 10, chance_of_light: int = 1):
    """crée un arc-en-ciel et le mélange en bogo sort

    Args:
        wait_ms (int): temps d'attente entre chaque mélange en ms
        durations_s (int): temps total d'éxécution
        chance_of_lighting (int): proba qu'une LED soit allumée (entre 0 et 1)
    """
    _bogo_controller(
        strip, wait_ms=wait_ms, duration_s=durations_s, chance_of_light=chance_of_light
    )
