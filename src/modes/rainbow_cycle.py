import time

from .utils.color_wheel import color_wheel


def _rainbow_cycle_controller(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(
                i, color_wheel((int(i * 256 / strip.numPixels()) + j) & 255)
            )
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbow_cycle(strip, wait_ms: int = 20, iterations: int = 5):
    """Allume la bande en arc-en-ciel qui tourne lentement

    Args:
        wait_ms (int): le temps d'attente entre chaque rotation
        iterations (int): Le nombre de tour à faire
    """
    _rainbow_cycle_controller(strip, wait_ms=wait_ms, iterations=iterations)
