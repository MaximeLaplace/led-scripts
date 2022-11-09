import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def strobo(
    strip,
    color=Color(255, 255, 255),
    wait_ms=50,
    duration_s: int = 10,
    infinite: bool = False,
):
    """Crée un strobo

    Args:
        color (tuple[int, int, int]): La couleur du strobo
        wait_ms (int): Le temps d'attente entre chaque flash en millisecondes
        duration_s (int): Combien de temps au total en secondes
    """
    time_left = init_time(duration_s)

    offset = 0
    segments = (1, 5)

    while time_left() > 0 or infinite:
        for segment in segments:
            (strip.segments[s].setColor(0) for s in segments)

            for i in range(offset, strip.segments[segment].numPixels(), 2):
                strip.segments[segment].setPixelColor(i, color)

            strip.show()
            time.sleep(wait_ms / 1000)

            strip.segments[segment].setColor(0)
            strip.show()

            time.sleep(wait_ms / 1000)
        offset = -1 * offset + 1

    return
