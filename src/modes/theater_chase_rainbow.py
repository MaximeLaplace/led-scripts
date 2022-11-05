import time

from .utils.color_wheel import color_wheel


def _theater_chase_rainbow_controller(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color_wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def theater_chase_rainbow(strip, wait_ms: int = 50):
    _theater_chase_rainbow_controller(strip, wait_ms=wait_ms)
