import time
from rpi_ws281x import Color

from .utils.init_time import init_time
from .utils.rainbow import create_rainbow_array, shift
from .utils.rainbowDemo import shrink, overlay, mix, color_array, half


def rainbowDemo(
    strip,
    wait_ms: int = 50,
    duration_s: int = 10,
    infinite: bool = True,
):
    rainbow_array = create_rainbow_array(strip)
    half_rainbow_array = create_rainbow_array(strip)
    half(half_rainbow_array)
    arrays = [half_rainbow_array, rainbow_array]
    ratios = [0, 100]
    asc = True

    time_left = init_time(duration_s)

    while time_left() > 0 or infinite:
        mix_array = mix(arrays, ratios)
        strip.setArrayColor(mix_array)
        strip.show()
        shift(rainbow_array)
        shift(half_rainbow_array)
        if asc:
            ratios[0] += 1
            if ratios[0] == 100:
                asc = False
        else:
            ratios[0] -= 1
            if ratios[0] == 0:
                asc = True
        time.sleep(wait_ms / 1000.0)
