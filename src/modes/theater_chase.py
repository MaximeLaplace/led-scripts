import time

from rpi_ws281x import Color


def _theater_chase_controller(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def theater_chase(
    strip, color: tuple[int, int, int], wait_ms: int = 50, iterations: int = 10
):
    _theater_chase_controller(
        strip, Color(*color), wait_ms=wait_ms, iterations=iterations
    )
