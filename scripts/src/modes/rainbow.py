import time

from .utils.init_time import init_time
from .utils.rainbow import create_rainbow_array, shift


def rainbow(
    strip,
    wait_ms: int = 50,
    duration_s: int = 10,
    infinite: bool = True,
):
    """Allume la bande en arc-en-ciel qui tourne lentement

    Args:
        wait_ms (int): le temps d'attente entre chaque rotation
        duration_s (int): le temps total
        inifinite (bool): run le script à l'infini
    """
    rainbow_array = create_rainbow_array(strip)

    time_left = init_time(duration_s)

    while time_left() > 0 or infinite:
        strip.setArrayColor(rainbow_array)
        strip.show()
        shift(rainbow_array)
        time.sleep(wait_ms / 1000.0)
