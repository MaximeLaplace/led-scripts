import time

from .utils.address_led_with_array import address_led_with_array
from .utils.color_wheel import color_wheel, create_rainbow_array
from .utils.init_time import init_time
from .utils.reset_strip import reset_strip


def theater_chase_rainbow(
    strip, wait_ms: int = 50, duration_s: int = 10, infinite: bool = False
):
    """Des petites lights qui tournent en étant en arc-en-ciel

    Args:
        wait_ms (int): Le temps d'attente entre chaque step en ms (petit = rapide)
    """
    time_left = init_time(duration_s)
    rainbow_array = create_rainbow_array(strip)

    while time_left() > 0 or infinite:
        for offset in range(3):
            reset_strip(strip)
            for i in range(offset, strip.numPixels(), 3):
                strip.setPixelColor(i, rainbow_array[i])
            strip.show()
            rainbow_array.append(rainbow_array.pop(0))
            time.sleep(wait_ms / 1000)
