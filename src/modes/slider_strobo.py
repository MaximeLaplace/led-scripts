import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def slider_strobo(
    strip,
    colour_begin: tuple[int, int, int] = (125, 125, 125),
    # color_end: tuple[int, int, int] = (255, 125, 125),
    length_slider: int = 30,
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
    r, b, g = colour_begin
    colour_gradient = [
        (
            k * r // (length_slider + 1),
            k * b // (length_slider + 1),
            k * g // (length_slider + 1),
        )
        for k in range(length_slider + 1, 0, -1)
    ]
    while time_left() > 0 or infinite:
        num_pixel = strip.segments[1].numPixels()
        for index_front in range(num_pixel):
            for index_stripe in range(min(index_front, length_slider)):
                strip.segments[1].setPixelColor(
                    index_front - index_stripe, Color(*colour_gradient[index_stripe])
                )
                strip.segments[5].setPixelColor(
                    num_pixel - (index_front - index_stripe) - 1,
                    Color(*colour_gradient[index_stripe]),
                )

            if index_front >= length_slider:
                strip.segments[1].setPixelColor(
                    index_front - length_slider, Color(0, 0, 0)
                )
                strip.segments[5].setPixelColor(
                    num_pixel - (index_front - length_slider) - 1, Color(0, 0, 0)
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


def gradient_at_position(index_beginning, length_slider, current_index, colour):

    return color_at_position


# idées - vitesse aleatoire de defilement
# - faire un dégradé de couleur entre couleur début et couleur fin
# - faire un fade in fade out
