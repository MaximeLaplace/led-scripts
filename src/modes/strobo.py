import time

from rpi_ws281x import Color
from src.modes.utils.reset_strip import reset_strip

from .utils.init_time import init_time


def _strobo_controller(
    strip,
    color=Color(255, 255, 255),
    wait_ms=50,
    duration_s: int = 10,
    infinite: bool = False,
):
    """stroboscope lights"""
    time_left = init_time(duration_s)

    while time_left() > 0 or infinite:

        for led in range(13, 50, 2):
            strip.setPixelColor(led, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        reset_strip(strip)
        time.sleep(wait_ms / 1000.0)

        for led in range(78, 115, 2):
            strip.setPixelColor(led, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        reset_strip(strip)
        time.sleep(wait_ms / 1000.0)

        for led in range(14, 50, 2):
            strip.setPixelColor(led, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        reset_strip(strip)
        time.sleep(wait_ms / 1000.0)

        for led in range(79, 115, 2):
            strip.setPixelColor(led, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        reset_strip(strip)
        time.sleep(wait_ms / 1000.0)


def strobo(
    strip,
    color: tuple[int, int, int] = (255, 255, 255),
    wait_ms: int = 50,
    duration_s: int = 10,
    infinite: bool = False,
) -> None:
    """Crée un strobo

    Args:
        color (tuple[int, int, int]): La couleur du strobo
        wait_ms (int): Le temps d'attente entre chaque flash en millisecondes
        duration_s (int): Combien de temps au total en secondes
    """
    _strobo_controller(
        strip, Color(*color), wait_ms=wait_ms, duration_s=duration_s, infinite=infinite
    )
