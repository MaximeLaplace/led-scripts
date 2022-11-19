from rpi_ws281x import Color

from .bogo import bogo
from .bouncing_pulse import bouncing_pulse
from .bubble_sort import bubble_sort
from .cellular_automaton import cellular_automaton
from .color_wipe import color_wipe
from .impact import impact
from .lamp import lamp
from .pulse import pulse
from .rainbow import rainbow
from .rainbowDemo import rainbowDemo
from .segment_strobo import segment_strobo
from .strobo import strobo
from .theater_chase import theater_chase
from .theater_chase_rainbow import theater_chase_rainbow


def demo(strip):
    while True:
        rainbow(strip=strip, duration_s=10)

        theater_chase_rainbow(strip=strip, duration_s=10)
        rainbowDemo(strip=strip, duration_s=10)

        impact(strip=strip, min_speed=0, max_speed=0, duration_s=5)
        impact(strip=strip, min_speed=-1, max_speed=1, duration_s=5)
        impact(strip=strip, min_speed=0, max_speed=2, duration_s=5)
        impact(strip=strip, min_speed=-1, max_speed=1, duration_s=5)
        impact(strip=strip, min_speed=-2, max_speed=0, duration_s=5)

        try:
            bouncing_pulse(strip=strip, iterations=300, infinite=False)
        except:
            pass

        for _ in range(3):
            theater_chase(strip=strip, color=(255, 0, 0), duration_s=1)
            theater_chase(strip=strip, color=(125, 125, 0), duration_s=1)
            theater_chase(strip=strip, color=(0, 255, 0), duration_s=1)
            theater_chase(strip=strip, color=(0, 125, 125), duration_s=1)
            theater_chase(strip=strip, color=(0, 0, 255), duration_s=1)
            theater_chase(strip=strip, color=(125, 0, 125), duration_s=1)

        strobo(strip=strip, wait_ms=120, duration_s=10)

        color_wipe(strip=strip, color=(255, 0, 0), wait_ms=25, duration_s=2)
        color_wipe(strip=strip, color=(0, 255, 0), wait_ms=25, duration_s=2)
        color_wipe(strip=strip, color=(0, 0, 255), wait_ms=25, duration_s=2)
