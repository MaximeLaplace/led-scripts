import random
import time

from .utils.rainbow import create_rainbow_array


def _swap_values(i: int, j: int):
    def inner(array):
        array[i], array[j] = array[j], array[i]

    return inner


def bubble_sort_array(array):
    new_array = [(i, c) for i, c in array]

    end_index = len(new_array) - 1
    current_index = 0

    while end_index != 0:
        if new_array[current_index] > new_array[current_index + 1]:
            _swap_values(current_index, current_index + 1)(new_array)
        current_index += 1
        if current_index == end_index:
            end_index -= 1
            current_index = 0
        yield [color for _, color in new_array]


def bubble_sort(strip, wait_ms: int = 2, rounds: int = 1, infinite: bool = False):
    rainbow_array = list(enumerate(create_rainbow_array(strip)))
    random.shuffle(rainbow_array)

    rounds_left = rounds

    while rounds_left > 0 or infinite:
        for array_state in bubble_sort_array(rainbow_array):
            strip.setArrayColor(array_state)
            strip.show()
            time.sleep(wait_ms / 1000)

        rounds_left -= 1
        random.shuffle(rainbow_array)
