import time

from .utils.init_time import init_time


def pulsating(
    strip,
    main_color: tuple[int, int, int] = (255, 0, 0),
    wait_ms: int = 50,
    infinite: bool = False,
):
    """Bande dont l'intensité est plus forte au milieu qui tourne

    Args:
        wait_ms (int): le temps d'attente entre chaque rotation
        duration_s (int): le temps total
        inifinite (bool): run le script à l'infini
    """
    time_left = init_time(duration_s)

    r,g,b = main_color
    color_gradient = [ (k*r//10, k*g//10, k*b//10)
        for k in list(range(1,10,2)) + list(range(1,10,2))[::-1]
    ]

    while infinite or time_left() > 0:
        for i in range(strip.numPixels()):
            for q in range(10): # Length of the band
                strip.setPixelColor((i+q)%strip.numPixels(), color_gradient(q))
        strip.show()
        time.sleep(wait_ms / 1000.0)
