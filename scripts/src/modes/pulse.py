import time

from rpi_ws281x import Color


def color_gradient(segment_length: int, main_color: tuple):
    """Gradient de couleur linéaire avec maximum au milieu et un offset pour ne pas avoir de valeurs trop sombres"""
    r, b, g = main_color
    offset = 3

    if segment_length % 2 == 0:
        return [
            (
                k * r // (segment_length + offset),
                k * b // (segment_length + offset),
                k * g // (segment_length + offset),
            )
            for k in list(range(1 + offset, segment_length + offset, 2))
            + list(range(segment_length + offset - 1, offset, -2))
        ]
    return [
        (
            k * r // (segment_length + offset),
            k * b // (segment_length + offset),
            k * g // (segment_length + offset),
        )
        for k in list(range(1 + offset, segment_length + offset, 2))
        + list(range(segment_length + offset, offset, -2))
    ]


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
    while iterations > 0 or infinite:
        for i in range(strip.numPixels()):
            # reset the previous led
            strip.setPixelColor((i - 1) % strip.numPixels(), Color(0, 0, 0))
            for q in range(10):  # Length of the band
                r, g, b = color_gradient(segment_length, main_color)[q]
                strip.setPixelColor((i + q) % strip.numPixels(), Color(r, g, b))
            strip.show()
            time.sleep(wait_ms / 1000.0)

        iterations -= 1
