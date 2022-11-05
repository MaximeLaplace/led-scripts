import time

from rpi_ws281x import Color
from src.strip_utils.reset_strip import reset_strip


def _strobo_controller(strip, color=Color(255, 255, 255), wait_ms=50, duration_s=10):
    """stroboscope lights"""
    current_time_s = 0
    while current_time_s <= duration_s:
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
        current_time_s += 4 * wait_ms / 1000.0


def strobo(
    strip,
    color: tuple[int, int, int] = (255, 255, 255),
    wait_ms: int = 50,
    duration_s: int = 10,
) -> None:
    _strobo_controller(strip, Color(*color), wait_ms=wait_ms, duration_s=duration_s)
