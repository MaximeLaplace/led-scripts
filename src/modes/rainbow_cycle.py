import time

from .utils.color_wheel import color_wheel
from .utils.init_time import init_time


def _rainbow_cycle_controller(
    strip, wait_ms=20, iterations=5, duration_s: int = 10, infinite: bool = False
):
    """Draw rainbow that uniformly distributes itself across all pixels."""

    time_left = init_time(duration_s)

    while time_left() > 0 or infinite:
        for j in range(256 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(
                    i, color_wheel((int(i * 256 / strip.numPixels()) + j) & 255)
                )
            strip.show()
            time.sleep(wait_ms / 1000.0)


def rainbow_cycle(
    strip,
    wait_ms: int = 20,
    iterations: int = 5,
    duration_s: int = 10,
    infinite: bool = False,
):
    """Allume la bande en arc-en-ciel qui tourne lentement

    Args:
        wait_ms (int): le temps d'attente entre chaque rotation
        iterations (int): Le nombre de tour à faire
    """
    _rainbow_cycle_controller(
        strip,
        wait_ms=wait_ms,
        iterations=iterations,
        duration_s=duration_s,
        infinite=infinite,
    )
