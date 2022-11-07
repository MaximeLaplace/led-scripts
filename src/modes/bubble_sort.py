import random
import time

from rpi_ws281x import Color

from .utils.address_led_with_array import address_led_with_array
from .utils.color_wheel import create_rainbow_array


def bubble_sort(strip, wait_ms: int = 100, infinite: bool = False):
    rainbow_array = create_rainbow_array(strip)

    index = 0

    while True:
        for i in range(8):
            strip.segments[i].setColor(Color(0, 0, 0))
        strip.segments[index % 8].setColor(Color(125, 125, 125))
        strip.show()
        index += 1
        time.sleep(wait_ms / 1000)
