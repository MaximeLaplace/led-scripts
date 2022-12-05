import time
from random import choice

from rpi_ws281x import Color

from .utils.init_time import init_time


def slider_strobo(
    strip,
    colour_begin: tuple[int, int, int] = (255, 0, 0),
    colour_end: tuple[int, int, int] = (0, 255, 0),
    length_slider: int = 20,
    wait_ms: int = 5,
    duration_s: int = 10,
    random_speeds: bool = False,
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

    list_possible_waits = [
        wait_ms / 4 + k * (4 * wait_ms - wait_ms / 4) / 10 for k in range(10)
    ]

    r_begin, b_begin, g_begin = colour_begin
    r_end, b_end, g_end = colour_end
    colour_gradient = [
        (
            int(
                k
                * (
                    r_begin
                    + ((length_slider + 1 - k) * (r_end - r_begin) / length_slider)
                )
                // (length_slider + 1)
            ),
            int(
                k
                * (
                    b_begin
                    + ((length_slider + 1 - k) * (b_end - b_begin) / length_slider)
                )
                // (length_slider + 1)
            ),
            int(
                k
                * (
                    g_begin
                    + ((length_slider + 1 - k) * (g_end - g_begin) / length_slider)
                )
                // (length_slider + 1)
            ),
        )
        for k in range(length_slider + 1, 0, -1)
    ]
    while time_left() > 0 or infinite:
        num_pixel = strip.segments[1].numPixels()
        current_wait = wait_ms
        if random_speeds:
            current_wait = choice(list_possible_waits)
        for index_front in range(
            num_pixel
        ):  # index_front is the index of the beginning of the slider
            for index_stripe in range(min(index_front + 1, length_slider)):
                # we iterate through the length of the slider and use the gradient list for the colors
                # we use the min to avoid going out of range when the slider is not completely full
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
            time.sleep(current_wait / 1000)

        for i in range(0, length_slider):
            strip.segments[1].shiftColors()
            strip.segments[5].shiftColors(direction=-1)

            strip.segments[1].setPixelColor(0, Color(0, 0, 0))
            strip.segments[5].setPixelColor(
                strip.segments[5].numPixels() - 1, Color(0, 0, 0)
            )
            time.sleep(current_wait / 1000)
            strip.show()
        time.sleep(25 * wait_ms / 1000)
    return
