import time
from random import choice

from rpi_ws281x import Color

from .utils.init_time import init_time


def gradient_coeff(k, total_k):  # triangular coefficients
    return 1 - abs(2 * (k / total_k) - 1)


def gradient_blink(
    strip,
    colour_begin: tuple[int, int, int] = (255, 0, 0),
    colour_end: tuple[int, int, int] = (0, 255, 0),
    wait_ms: int = 20,
    duration_s: int = 10,
    n_steps_gradiant: int = 30,
    random_speeds: bool = False,
    infinite: bool = True,
):
    """Crée un degradé temporel qui clignote

    Args:
        colour_begin: tuple[int, int, int], couleur de début
        colour_end: tuple[int, int, int], couleur de fin
        wait_ms (int): Le temps d'attente entre chaque update en millisecondes
        duration_s (int): Combien de temps au total en secondes
        n_steps_gradiant (int): number of steps in the gradiant
    """
    time_left = init_time(duration_s)

    segments_one = (1, 5)
    segments_two = (2, 6)
    list_segment = [segments_one, segments_two]

    list_possible_waits = [
        wait_ms / 4 + k * (4 * wait_ms - wait_ms / 4) / 10 for k in range(10)
    ]

    r_begin, b_begin, g_begin = colour_begin
    r_end, b_end, g_end = colour_end
    colour_gradient = [
        (
            (
                r_begin
                + ((n_steps_gradiant + 1 - k) * (r_end - r_begin) / n_steps_gradiant)
            ),
            (
                b_begin
                + ((n_steps_gradiant + 1 - k) * (b_end - b_begin) / n_steps_gradiant)
            ),
            (
                g_begin
                + ((n_steps_gradiant + 1 - k) * (g_end - g_begin) / n_steps_gradiant)
            ),
        )
        for k in range(n_steps_gradiant + 1, 0, -1)
    ]
    colour_gradient = [
        (
            int(gradient_coeff(k, n_steps_gradiant) * colour_gradient[k][0]),
            int(gradient_coeff(k, n_steps_gradiant) * colour_gradient[k][1]),
            int(gradient_coeff(k, n_steps_gradiant) * colour_gradient[k][2]),
        )
        for k in range(len(colour_gradient))
    ]
    current_wait = wait_ms
    if random_speeds:
        current_wait = choice(list_possible_waits)
    while time_left() > 0 or infinite:
        strip.reset()
        for color in colour_gradient:
            strip.segments[1].setColor(Color(*color))
            strip.segments[5].setColor(Color(*color))
            strip.show()
            time.sleep(current_wait / 1000)
        time.sleep(current_wait / 1000)
        strip.reset()
        for color in colour_gradient:
            strip.segments[2].setColor(Color(*color))
            strip.segments[6].setColor(Color(*color))
            strip.show()
            time.sleep(current_wait / 1000)
        strip.show()
        time.sleep(current_wait / 1000)

    return
