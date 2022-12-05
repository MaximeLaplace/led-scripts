import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def _color_wipe_controller(
    strip, color, wait_ms=50, duration_s: int = 10, infinite: bool = True
):
    time_left = init_time(duration_s)

    while time_left() > 0 or infinite:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
            strip.show()
            time.sleep(wait_ms / 1000)


def color_wipe(
    strip,
    color: tuple[int, int, int] = (255, 0, 0),
    wait_ms: int = 50,
    duration_s: int = 10,
    infinite: bool = True,
):
    """Allume la bande lumineuse progressivement

    Args:
        color (tuple[int, int, int]): La couleur utilisée.
        wait_ms (int): le temps d'attente entre les allumages de 2 LED consécutives.
    """
    _color_wipe_controller(
        strip, Color(*color), wait_ms=wait_ms, duration_s=duration_s, infinite=infinite
    )
