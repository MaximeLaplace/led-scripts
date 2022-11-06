import random
import time

from .utils.address_led_with_array import address_led_with_array
from .utils.color_wheel import create_rainbow_array


def bubble_sort(strip, wait_ms: int = 100, infinite: bool = False):
    rainbow_array = create_rainbow_array(strip)

    while True:
        address_led_with_array(strip, rainbow_array)
        strip.show()
        first = rainbow_array.pop(0)
        rainbow_array.append(first)
        time.sleep(wait_ms / 1000)
