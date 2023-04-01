import time
from random import randint

from rpi_ws281x import Color


def hue_to_rgb(hue: int):
    """Renvoie la valeur RGB d'une teinte donnée avec 100% de saturation et 50% de luminosité"""
    h = hue / 60
    X = int(255 * (1 - abs(h % 2 - 1)))
    if 0 <= h < 1:
        return (255, 0, X)
    if 1 <= h < 2:
        return (X, 0, 255)
    if 2 <= h < 3:
        return (0, X, 255)
    if 3 <= h < 4:
        return (0, 255, X)
    if 4 <= h < 5:
        return (X, 255, 0)
    if 5 <= h < 6:
        return (255, X, 0)


def modulo_range(strip, beg: int, end: int):
    """Prends deux indices and renvoie la liste des indices entre eux modulo le nombre de pixels
    Utile lorsqu'une bande est au bout de la strip de leds"""
    if beg > end:
        beg -= strip.numPixels()
    return [x % strip.numPixels() for x in range(beg, end)]


def is_overlapping(strip, band_1: tuple, band_2: tuple):
    """Dit si deux bandes se chevauchent"""
    for x in modulo_range(strip, *band_1):
        if x in [y for y in modulo_range(strip, *band_2)]:
            return True
    return False


def color_gradient(strip, beg: int, end: int, main_color: tuple):
    """Gradient de couleur linéaire avec maximum au milieu et un offset pour ne pas avoir de valeurs trop sombres"""
    r, b, g = main_color
    segment_length = len(modulo_range(strip, beg, end))
    offset = 3

    if segment_length % 2 == 0:
        return [
            Color(
                k * r // (segment_length + offset),
                k * b // (segment_length + offset),
                k * g // (segment_length + offset),
            )
            for k in list(range(1 + offset, segment_length + offset, 2))
            + list(range(segment_length + offset - 1, offset, -2))
        ]
    return [
        Color(
            k * r // (segment_length + offset),
            k * b // (segment_length + offset),
            k * g // (segment_length + offset),
        )
        for k in list(range(1 + offset, segment_length + offset, 2))
        + list(range(segment_length + offset, offset, -2))
    ]


def bouncing_pulse(
    strip,
    segment_length: int = 11,
    wait_ms: int = 50,
    iterations: int = 10,
    infinite: bool = True,
):
    """Deux bandes qui se rebondissent dessus de couleur et vitesse changeant à chaque collision

    Args:
        segment_length (int): nombre de leds allumées simultanéments
        wait_ms (int): le temps d'attente entre chaque déplacement
        iterations (int): Le nombre de mouvement effectués
        infinite (bool): run le script à l'infini
    """

    # Initialisation des positions des bandes : index de début et index de fin de la bande
    fir_band_pos = (
        strip.numPixels() - segment_length // 2,
        segment_length - segment_length // 2,
    )  # Centré à l'index 0
    sec_band_pos = (
        strip.numPixels() // 2 - segment_length // 2,
        strip.numPixels() // 2 + segment_length - segment_length // 2,
    )  # Centré au milieu du strip de leds

    speeds = (2, -2)  # Initialisation des vitesses
    h1, h2 = (randint(0, 359), randint(0, 359))  # Teintes aléatoires
    colors = [hue_to_rgb(h1), hue_to_rgb(h2)]  # Initialisation des couleurs

    while infinite or iterations > 0:
        # Mise à noir de tous les pixels colorés
        for index in modulo_range(strip, *fir_band_pos) + modulo_range(
            strip, *sec_band_pos
        ):
            strip.setPixelColor(index, Color(0, 0, 0))

        # On avance les bandes
        fir_band_pos = tuple(
            (bound + speeds[0]) % strip.numPixels() for bound in fir_band_pos
        )
        sec_band_pos = tuple(
            (bound + speeds[1]) % strip.numPixels() for bound in sec_band_pos
        )

        # On teste si les deux bandes se rentrent dedans
        if is_overlapping(strip, fir_band_pos, sec_band_pos):
            while is_overlapping(strip, fir_band_pos, sec_band_pos):
                # On recule les bandes de 1 cases chacune jusqu'à ce qu'elles ne se chevauchent plus
                fir_band_pos = tuple(
                    (bound - (speeds[0] // abs(speeds[0]))) % strip.numPixels()
                    for bound in fir_band_pos
                )
                sec_band_pos = tuple(
                    (bound - (speeds[1] // abs(speeds[1]))) % strip.numPixels()
                    for bound in sec_band_pos
                )
            # Nouvelles vitesses (dans des sens différents)
            speeds = [randint(1, 5) * (-speed // abs(speed)) for speed in speeds]

            h1, h2 = (randint(1, 360), randint(1, 360))  # Nouvelles teintes
            colors = [hue_to_rgb(h1), hue_to_rgb(h2)]  # Nouvelles couleurs

        # On allume les leds
        fir_colors = color_gradient(strip, *fir_band_pos, main_color=colors[0])
        sec_colors = color_gradient(strip, *sec_band_pos, main_color=colors[1])

        for i, index in enumerate(modulo_range(strip, *fir_band_pos)):
            strip.setPixelColor(index, fir_colors[i])
        for i, index in enumerate(modulo_range(strip, *sec_band_pos)):
            strip.setPixelColor(index, sec_colors[i])

        # On update les couleurs
        strip.show()
        time.sleep(wait_ms / 1000.0)

        iterations -= 1
