import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def _theater_chase_controller(
    strip,
    color,
    wait_ms=50,
    iterations=10,
    duration_s: int = 10,
    infinite: bool = True,
):
    """Movie theater light style chaser animation."""
    time_left = init_time(duration_s)

    while time_left() > 0 or infinite:
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    if i + q < strip.numPixels():
                        strip.setPixelColor(i + q, color)
                strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    if i + q < strip.numPixels():
                        strip.setPixelColor(i + q, 0)


def theater_chase(
    strip,
    color: tuple[int, int, int] = (0, 255, 0),
    wait_ms: int = 50,
    iterations: int = 10,
    duration_s: int = 10,
    infinite: bool = False,
):
    """Des petites lights qui tournent en étant d'une couleur au choix

    Args:
        color (tuple[int, int, int]): la couleur des LED
        wait_ms (int): Le temps d'attente entre chaque step en ms (petit = rapide)
        iterations (int): Le nombre de tours effectués
    """
    _theater_chase_controller(
        strip,
        Color(*color),
        wait_ms=wait_ms,
        iterations=iterations,
        duration_s=duration_s,
        infinite=infinite,
    )
