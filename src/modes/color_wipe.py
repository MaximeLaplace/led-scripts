import time

from rpi_ws281x import Color


def _color_wipe_controller(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def color_wipe(strip, color: tuple[int, int, int] = (255, 0, 0), wait_ms: int = 50):
    _color_wipe_controller(strip, Color(*color), wait_ms=wait_ms)
