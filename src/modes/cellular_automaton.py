import time

from rpi_ws281x import Color

from .utils.init_time import init_time


class CircularList(list):
    """List but you can have index and slices out of range"""
    def __getitem__(self, key):
        if isinstance(key, slice ) :
            # Get the start, stop, and step from the slice without ceiling the stop
            start, stop, step = key.indices(10**6)
            if stop < start and step > 0: # From left to right
                return [self[i] for i in range(start,stop+len(self),step)]
            elif stop > start and step < 0: # From right to left
                return [self[i] for i in range(start+len(self),stop,step)]
            else:
                return [self[i] for i in range(start,stop,step)]
        elif isinstance( key, int ) :
            return super(CircularList, self).__getitem__(key % len(self))
        else:
            raise TypeError("Invalid argument type.")


def tertiary_decomposition(x):
    decomposition = []
    for pow in [3**k for k in range(6,-1,-1)]:
        if x >= 2*pow:
            decomposition.append(2)
            x -= 2*pow
        elif x >= pow:
            decomposition.append(1)
            x -= pow
        else:
            decomposition.append(0)
    return decomposition


def cellular_automaton(
    strip,
    color: tuple[int, int, int] = (127, 255, 0),
    rule: int = 948,
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

    r,b,g = color
    main_color = Color(r,b,g)
    gray_color = Color(r//2,b//2,g//2)

    leds_status = CircularList([1]*strip.numPixels()) # Array de 0,1,2
    leds_status[0] = 1 # Position initiale
    strip.setPixelColor(0, gray_color)
    strip.show()
    time.sleep(wait_ms / 1000.0)

    tertiary = tertiary_decomposition(rule)[::-1]

    while time_left() or infinite:
        for i in range(strip.numPixels()):
            s = sum(leds_status[i-1:i+2])
            if tertiary[s] == 2:
                strip.setPixelColor(i, main_color)
                leds_status[i] = 2
            elif tertiary[s] == 1:
                strip.setPixelColor(i, gray_color)
                leds_status[i] = 1
            else:
                strip.setPixelColor(i, Color(0,0,0))
                leds_status[i] = 0
        strip.show()
        time.sleep(wait_ms / 1000.0)
