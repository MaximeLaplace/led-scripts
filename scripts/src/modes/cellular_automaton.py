import time

from rpi_ws281x import Color

from .utils.init_time import init_time
from .utils.circular_list import CircularList


def tertiary_decomposition(x):
    decomposition = []
    for pow in [3**k for k in range(6, -1, -1)]:
        if x >= 2 * pow:
            decomposition.append(2)
            x -= 2 * pow
        elif x >= pow:
            decomposition.append(1)
            x -= pow
        else:
            decomposition.append(0)
    return decomposition[::-1]  # To have the lower power on the left


def cellular_automaton(
    strip,
    color: tuple[int, int, int] = (255, 255, 0),
    rule: int = 912,
    wait_ms: int = 50,
    duration_s: int = 10,
    infinite: bool = True,
):
    """Automate cellulaire 1d tricolore (chaque led peut être éteinte, allumée ou à moitié allumée)

    Args:
        color (tuple[int, int, int]) : couleur
        rule (int): règle d'automate cellulaire 1D, il y a 3^7 = 2187 règles possibles
        wait_ms (int): le temps d'attente entre chaque déplacement
        duration_s (int): Combien de temps au total en secondes
        infinite (bool): run le script à l'infini
    """
    time_left = init_time(duration_s)

    r, b, g = color
    number_to_color = {
        0: Color(0, 0, 0),
        1: Color(r // 2, b // 2, g // 2),
        2: Color(r, b, g),
    }

    leds_status = CircularList([1] * strip.numPixels())  # Array de 0,1,2
    leds_status[0] = 1  # Position initiale

    tertiary = tertiary_decomposition(rule)

    while infinite or time_left():
        for i in range(strip.numPixels()):
            s = sum(leds_status[i - 1 : i + 2])
            strip.setPixelColor(i, number_to_color[tertiary[s]])
            leds_status[i] = tertiary[s]
        strip.show()
        time.sleep(wait_ms / 1000.0)
