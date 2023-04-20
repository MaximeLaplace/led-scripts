import time

from rpi_ws281x import Color

from ..utils.init_time import init_time
from ..utils.rainbow import shift
from ..utils.kanopeeUtils import map_letters


def kano_strobo(
    strip, color=(255, 255, 255), wait_ms: int = 100, duration_s: int = 10, infinite: bool = True
):
    time_left = init_time(duration_s)

    on_color = Color(*color)
    off_color = Color(0, 0, 0)
    strip_length = strip.numPixels()
    half_array = [off_color]*strip_length

    for i in range(0, strip_length, 2):
        half_array[i] = on_color

    while time_left() > 0 or infinite:
        strip.setArrayColor(half_array)
        strip.show()
        time.sleep(wait_ms / 1000)
        strip.setArrayColor([off_color]*strip_length)
        strip.show()
        time.sleep(wait_ms / 1000)
        half_array = invert(half_array, on_color, off_color)

def invert(array, colorA, colorB):
    for i in range(len(array)):
        if array[i] == colorA:
            array[i] = colorB
        elif array[i] == colorB:
            array[i] = colorA
    return array
