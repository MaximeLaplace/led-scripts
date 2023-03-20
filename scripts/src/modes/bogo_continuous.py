import random
import time

from rpi_ws281x import Color

from .utils.init_time import init_time
from .utils.rainbow import create_rgb_rainbow_array


def gradient_coeff(k, total_k):  # triangular coefficients
    return 1 - abs(2 * (k / total_k) - 1)


def compute_gradient_between(color_a, color_b, number_of_steps: int):
    r_begin, b_begin, g_begin = color_a
    r_end, b_end, g_end = color_b
    colour_gradient = [
        (
            int(
                r_begin
                + ((number_of_steps + 1 - k) * (r_end - r_begin) / number_of_steps)
            ),
            int(
                b_begin
                + ((number_of_steps + 1 - k) * (b_end - b_begin) / number_of_steps)
            ),
            int(
                g_begin
                + ((number_of_steps + 1 - k) * (g_end - g_begin) / number_of_steps)
            ),
        )
        for k in range(number_of_steps + 1, 0, -1)
    ]
    # colour_gradient = [
    #     (
    #         int(gradient_coeff(k, number_of_steps) * colour_gradient[k][0]),
    #         int(gradient_coeff(k, number_of_steps) * colour_gradient[k][1]),
    #         int(gradient_coeff(k, number_of_steps) * colour_gradient[k][2]),
    #     )
    #     for k in range(len(colour_gradient))
    # ]
    return colour_gradient


def _bogo_continuous_controller(strip, wait_ms: int = 1000, nodes_number: int = 10):
    while True:
        strip.reset()
        length = strip.numPixels()

        segment_length = int(length / nodes_number)

        random_start = random.randint(0, length - 1)
        indices = [
            (random_start + i * segment_length) % length for i in range(nodes_number)
        ]

        rainbow_array = create_rgb_rainbow_array(strip)

        node_colors = [rainbow_array[index] for index in indices]
        random.shuffle(node_colors)

        for index, [led_number, color] in enumerate(zip(indices, node_colors)):
            next_color = node_colors[(index + 1) % len(node_colors)]
            next_led_number = indices[(index + 1) % len(node_colors)]

            if next_led_number < led_number:
                next_led_number += length

            seg_length = next_led_number - led_number

            colour_gradient = compute_gradient_between(color, next_color, seg_length)

            for i, led in enumerate(range(led_number, next_led_number)):
                strip.setPixelColor(led % length, Color(*colour_gradient[i]))

        strip.show()
        time.sleep(wait_ms / 1000)


def bogo_continuous(
    strip,
    nodes_number: int = 10,
    wait_ms: int = 100,
):
    """crée un arc-en-ciel et le mélange en bogo sort

    Args:
        wait_ms (int): temps d'attente entre chaque mélange en ms
        durations_s (int): temps total d'éxécution
    """
    _bogo_continuous_controller(
        strip,
        wait_ms=wait_ms,
        nodes_number=nodes_number,
    )
