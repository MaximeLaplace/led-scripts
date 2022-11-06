import random

from rpi_ws281x import Color


def address_led_with_array(strip, array, chance_of_light: int = 1):
    """Allume les LED avec un array de couleurs et une proba d'allumage sur chaque LED

    Args:
        array (list[Color]): la liste des couleurs
        chance_of_light (int): la chance qu'une led soit allumée entre 0 et 1
    """
    if strip.numPixels() != len(array):
        raise (
            ValueError(
                f"L'array de couleur n'a pas autant de couleurs ({len(array)} couleurs) qu'il y a de LED sur la bande ({strip.numPixels()} LEDs) !"
            )
        )

    for i in range(len(array)):
        if random.random() < chance_of_light:
            strip.setPixelColor(i, array[i])
        else:
            strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
