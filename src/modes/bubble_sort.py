import random
import time

from .utils.address_led_with_array import address_led_with_array
from .utils.color_wheel import create_rainbow_array


def bubble_sort(strip, wait_ms: int = 100, infinite: bool = False):
    rainbow_array = create_rainbow_array(strip)
    # random.shuffle(rainbow_array)
    # rainbow_array.sort()

    address_led_with_array(strip, rainbow_array)
    strip.show()

    time.sleep(10)
