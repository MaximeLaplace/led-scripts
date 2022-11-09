import time

from rpi_ws281x import Color

from .utils.init_time import init_time


def pulsating(
    strip,
    main_color: tuple[int, int, int] = (255, 0, 0),
    wait_ms: int = 50,
    iterations: int = 1000,
    infinite: bool = True,
):
    """Bande dont l'intensité est plus forte au milieu qui tourne

    Args:
        main_color (tuple[int, int, int]) : couleur principale apparaissant (il n'y aura que des variations d'intensité)
        wait_ms (int): le temps d'attente entre chaque déplacement
        iterations (int): Le nombre de mouvement effectués
        infinite (bool): run le script à l'infini
    """
    r,g,b = main_color
    color_gradient = [ (k*r//10, k*g//10, k*b//10)
        for k in list(range(1,10,2)) + list(range(1,10,2))[::-1]
    ]

    while iterations > 0 or infinite:
        for i in range(strip.numPixels()):
            # reset the previous led
            strip.setPixelColor((i-1)%strip.numPixels(), Color(0,0,0))
            for q in range(10): # Length of the band
                r,g,b = color_gradient[q]
                print("led nb: ",(i+q)%strip.numPixels())
                strip.setPixelColor((i+q)%strip.numPixels(), Color(r,g,b))
        strip.show()
        time.sleep(wait_ms / 1000.0)

        iterations -= 1
