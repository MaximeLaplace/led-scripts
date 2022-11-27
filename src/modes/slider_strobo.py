import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def slider_strobo(
    strip,
    color_begin: tuple[int, int, int] = (125, 125, 125),
    # color_end: tuple[int, int, int] = (255, 125, 125),
    length_slider: int = 25,
    wait_ms: int = 10,
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
        num_pixel = strip.segments[1].numPixels()
        for i in range(num_pixel):
            strip.segments[1].setPixelColor(i, Color(*color_begin))
            strip.segments[5].setPixelColor(num_pixel - i - 1, Color(*color_begin))

            if i >= length_slider:
                strip.segments[1].setPixelColor(i - length_slider, Color(0, 0, 0))
                strip.segments[5].setPixelColor(
                    num_pixel - (i - length_slider) - 1, Color(0, 0, 0)
                )
            strip.show()
            time.sleep(wait_ms / 1000)

        for i in range(num_pixel - length_slider, num_pixel):
            strip.segments[1].setPixelColor(i, Color(0, 0, 0))
            strip.segments[5].setPixelColor(num_pixel - i - 1, Color(0, 0, 0))
            time.sleep(wait_ms / 1000)
            strip.show()
        time.sleep(25 * wait_ms / 1000)
    return
