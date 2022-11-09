import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def pulse(
    strip,
    main_color: tuple[int, int, int] = (255, 255, 0),
    segment_length: int = 12,
    wait_ms: int = 30,
    iterations: int = 10,
    infinite: bool = True,
):
    """Bande dont l'intensité est plus forte au milieu qui tourne

    Args:
        main_color (tuple[int, int, int]) : couleur principale apparaissant (il n'y aura que des variations d'intensité)
        segment_length (int): nombre de leds allumées simultanéments
        wait_ms (int): le temps d'attente entre chaque déplacement
        iterations (int): Le nombre de mouvement effectués
        infinite (bool): run le script à l'infini
    """
    r,g,b = main_color
    color_gradient = [ (k*r//segment_length, k*g//segment_length, k*b//segment_length)
        for k in list(range(1,segment_length,2)) + list(range(1,segment_length,2))[::-1]
    ]

    while iterations > 0 or infinite:
        for i in range(strip.numPixels()):
            # reset the previous led
            strip.setPixelColor((i-1)%strip.numPixels(), Color(0,0,0))
            for q in range(10): # Length of the band
                r,g,b = color_gradient[q]
                strip.setPixelColor((i+q)%strip.numPixels(), Color(r,g,b))
            strip.show()
            time.sleep(wait_ms / 1000.0)

        iterations -= 1
