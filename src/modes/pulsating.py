import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def pulsating(
    strip,
    main_color: tuple[int, int, int] = (255, 0, 0),
    wait_ms: int = 50,
    iterations: int = 10,
    infinite: bool = False,
):
    """Bande dont l'intensité est plus forte au milieu qui tourne

    Args:
        main_color (tuple[int, int, int]) : couleur principale apparaissant (il n'y aura que des variations d'intensité)
        wait_ms (int): le temps d'attente entre chaque rotation
        iterations (int): Le nombre de tours effectués
        inifinite (bool): run le script à l'infini
    """
    r,g,b = main_color
    color_gradient = [ (k*r//10, k*g//10, k*b//10)
        for k in list(range(1,10,2)) + list(range(1,10,2))[::-1]
    ]

    while infinite or iterations > 0:
        for i in range(strip.numPixels()):
            for q in range(10): # Length of the band
                strip.setPixelColor((i+q)%strip.numPixels(), Color(color_gradient[q]))
        strip.show()
        time.sleep(wait_ms / 1000.0)

        iterations -= 1
