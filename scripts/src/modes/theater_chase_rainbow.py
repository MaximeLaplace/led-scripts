import time

from .utils.init_time import init_time
from .utils.rainbow import create_rainbow_array, shift


def theater_chase_rainbow(
    strip, wait_ms: int = 50, duration_s: int = 10, infinite: bool = True
):
    """Des petites lights qui tournent en étant en arc-en-ciel

    Args:
        wait_ms (int): Le temps d'attente entre chaque step en ms (petit = rapide)
    """
    time_left = init_time(duration_s)
    rainbow_array = create_rainbow_array(strip)

    while time_left() > 0 or infinite:
        for offset in range(3):
            strip.reset()
            for i in range(offset, strip.numPixels(), 3):
                strip.setPixelColor(i, rainbow_array[i])
            strip.show()
            shift(rainbow_array)
            time.sleep(wait_ms / 1000)
