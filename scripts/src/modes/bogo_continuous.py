import random
import time

from rpi_ws281x import Color

from .utils.rainbow import create_rgb_rainbow_array


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
    return colour_gradient


def _bogo_continuous_controller(strip, wait_ms: int = 1, nodes_number: int = 10):
    strip.reset()

    length = strip.numPixels()

    segment_length = int(length / nodes_number)

    random_start = random.randint(0, length - 1)
    nodes_led_numbers = [
        (random_start + i * segment_length) % length for i in range(nodes_number)
    ]
    rainbow_array = create_rgb_rainbow_array(strip)
    node_colors = [rainbow_array[index] for index in nodes_led_numbers]
    random.shuffle(node_colors)

    while True:
        next_node_colors = node_colors.copy()
        random.shuffle(next_node_colors)

        nodes_gradients = []
        for [node_color, next_node_color] in zip(node_colors, next_node_colors):
            nodes_gradients.append(
                compute_gradient_between(node_color, next_node_color, 20)
            )
        nodes_gradients = [list(x) for x in list(zip(*nodes_gradients))]

        for t_step in range(20):

            current_node_colors = nodes_gradients[t_step]

            for index, [led_number, color] in enumerate(
                zip(nodes_led_numbers, current_node_colors)
            ):
                next_color = current_node_colors[(index + 1) % len(current_node_colors)]
                next_led_number = nodes_led_numbers[
                    (index + 1) % len(current_node_colors)
                ]

                if next_led_number < led_number:
                    next_led_number += length

                seg_length = next_led_number - led_number

                colour_gradient = compute_gradient_between(
                    color, next_color, seg_length
                )

                for i, led in enumerate(range(led_number, next_led_number)):
                    strip.setPixelColor(led % length, Color(*colour_gradient[i]))

            strip.show()
            time.sleep(wait_ms / 1000)

        node_colors = next_node_colors.copy()


def bogo_continuous(
    strip,
    nodes_number: int = 13,
    wait_ms: int = 1,
):
    """random * random"""
    _bogo_continuous_controller(
        strip,
        wait_ms=wait_ms,
        nodes_number=nodes_number,
    )
