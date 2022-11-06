import time

from .utils.color_wheel import color_wheel


def _rainbow_controller(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color_wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbow(strip, wait_ms: int = 20, iterations: int = 1):
    """Allume la bande de LED avec un arc-en-ciel statique

    Args:
        wait_ms (int): Aucune idée de ce que ça fait
        iterations (int): Pareil
    """
    _rainbow_controller(strip, wait_ms=wait_ms, iterations=iterations)
