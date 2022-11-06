def address_array(strip, array):
    """Allume les LED avec un array de couleurs

    Args:
        array (list[Color]): la liste des couleurs
    """
    if strip.numPixels() != len(array):
        raise (
            ValueError(
                f"L'array de couleur n'a pas autant de couleurs ({len(array)} couleurs) qu'il y a de LED sur la bande ({strip.numPixels()} LEDs) !"
            )
        )

    for i in range(len(array)):
        strip.setPixelColor(i, array[i])
    strip.show()
