import random
import time

from .utils.address_led_with_array import address_led_with_array
from .utils.color_wheel import create_color_rainbow_array
from .utils.init_time import init_time


def _bogo_controller(
    strip,
    wait_ms: int = 100,
    chance_of_light: float = 1.0,
    duration_s: int = 10,
    infinite: bool = False,
):
    time_left = init_time(duration_s)
    rainbow_array = create_color_rainbow_array(strip)

    while time_left() > 0 or infinite:
        random.shuffle(rainbow_array)
        address_led_with_array(strip, rainbow_array, chance_of_light=chance_of_light)
        strip.show()
        time.sleep(wait_ms / 1000)


def bogo(
    strip,
    wait_ms: int = 100,
    chance_of_light: float = 0.5,
    durations_s: int = 10,
    infinite: bool = False,
):
    """crée un arc-en-ciel et le mélange en bogo sort

    Args:
        wait_ms (int): temps d'attente entre chaque mélange en ms
        durations_s (int): temps total d'éxécution
        chance_of_lighting (int): proba qu'une LED soit allumée (entre 0 et 1)
    """
    _bogo_controller(
        strip,
        wait_ms=wait_ms,
        chance_of_light=chance_of_light,
        duration_s=durations_s,
        infinite=infinite,
    )
