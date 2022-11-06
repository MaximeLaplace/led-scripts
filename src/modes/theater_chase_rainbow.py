import time

from .utils.color_wheel import color_wheel
from .utils.init_time import init_time


def _theater_chase_rainbow_controller(
    strip,
    wait_ms=50,
    duration_s: int = 10,
    infinite: bool = False,
):
    """Rainbow movie theater light style chaser animation."""
    time_left = init_time(duration_s)

    while time_left() > 0 or infinite:
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, color_wheel((i + j) % 255))
                strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, 0)


def theater_chase_rainbow(
    strip,
    wait_ms: int = 50,
    duration_s: int = 10,
    infinite: bool = False,
):
    """Des petites lights qui tournent en étant en arc-en-ciel

    Args:
        wait_ms (int): Le temps d'attente entre chaque step en ms (petit = rapide)
    """
    _theater_chase_rainbow_controller(
        strip, wait_ms=wait_ms, duration_s=duration_s, infinite=infinite
    )
