import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def slider_strobo(
    strip,
    color_begin: tuple[int, int, int] = (255, 255, 255),
    # color_end: tuple[int, int, int] = (255, 125, 125),
    wait_ms: int = 5,
    duration_s: int = 10,
    infinite: bool = True,
):
    """Crée deux lignes qui s'étendent  sur les cotés et disparaissent

    Args:
        color (tuple[int, int, int]): La couleur, qui tendra vers
        wait_ms (int): Le temps d'attente entre chaque flash en millisecondes
        duration_s (int): Combien de temps au total en secondes
    """
    time_left = init_time(duration_s)

    segments = (1, 5)

    while time_left() > 0 or infinite:

        for i in range(strip.segments[1].numPixels()):
            strip.segments[1].setPixelColor(i, Color(*color_begin))
            strip.segments[5].setPixelColor(i, Color(*color_begin))
            time.sleep(wait_ms / 1000)
            strip.show()

        strip.segments[1].setColor(Color(0, 0, 0))
        strip.segments[5].setColor(Color(0, 0, 0))
        strip.show()

    return
