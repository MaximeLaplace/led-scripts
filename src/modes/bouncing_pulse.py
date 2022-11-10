import time
from random import randint

from rpi_ws281x import Color


def hue_to_rgb(hue: int): # 100% saturation and 50% lightness
    h = hue/60
    X = int(255*(1-abs(h%2-1)))
    if 0 <= h < 1:
        return (255,0,X)
    if 1 <= h < 2:
        return (X,0,255)
    if 2 <= h < 3:
        return (0,X,255)
    if 3 <= h < 4:
        return (0,255,X)
    if 4 <= h < 5:
        return (X,255,0)
    if 5 <= h < 6:
        return (255,X,0)

def modulo_range(strip, beg: int, end: int):
    if beg > end:
        beg -= strip.numPixels()
    return [x%strip.numPixels() for x in range(beg,end)]

def overlap(
        strip,
        band_1: tuple,
        band_2: tuple
    ):
    for x in modulo_range(strip,*band_1):
        if x in [y for y in modulo_range(strip,*band_2)]: return True
    return False

def color_gradient(strip, beg: int, end: int, main_color: tuple):
    r,b,g = main_color
    segment_length = len(modulo_range(strip, beg, end))
    return [Color(k*r//segment_length, k*b//segment_length, k*g//segment_length)
        for k in list(range(1,segment_length,2)) + list(range(1,segment_length,2))[::-1]
    ]


def bouncing_pulse(
    strip,
    segment_length: int = 7,
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
    # every index need to be in [0, strip.numPixels()]
    fir_band_pos = (strip.numPixels()-segment_length//2, segment_length-segment_length//2) # center around zero
    sec_band_pos = (strip.numPixels()//2-segment_length//2, strip.numPixels()//2+segment_length-segment_length//2) # center around middle position

    speeds = (2,-2)
    h1, h2 = (randint(0,359), randint(0,359)) # random hues
    colors = [hue_to_rgb(h1), hue_to_rgb(h2)]

    while infinite or iterations > 0:
        # reset the old pixels
        for index in modulo_range(strip,*fir_band_pos) + modulo_range(strip,*sec_band_pos):
            strip.setPixelColor(index, Color(0,0,0))

        # move bands forward
        fir_band_pos = tuple((bound+speeds[0])%strip.numPixels() for bound in fir_band_pos)
        sec_band_pos = tuple((bound+speeds[1])%strip.numPixels() for bound in sec_band_pos)

        # check collision
        if overlap(strip, fir_band_pos, sec_band_pos):
            while overlap(strip, fir_band_pos, sec_band_pos):
                # move bands back
                fir_band_pos = tuple((bound-(speeds[0]//abs(speeds[0])))%strip.numPixels() for bound in fir_band_pos)
                sec_band_pos = tuple((bound-(speeds[1]//abs(speeds[1])))%strip.numPixels() for bound in sec_band_pos)
            # random speed with opposite direction to previous speed
            speeds = [-speed*randint(1,6)//abs(speed) for speed in speeds]

            h1, h2 = (randint(1,360), randint(1,360)) # random hues
            colors = [hue_to_rgb(h1), hue_to_rgb(h2)]  

        # color leds
        fir_colors = color_gradient(strip, *fir_band_pos, main_color=colors[0])
        sec_colors = color_gradient(strip, *sec_band_pos, main_color=colors[1])
        for ind, pos in enumerate(modulo_range(strip,*fir_band_pos)):
            strip.setPixelColor(pos, fir_colors[ind])
        for ind, pos in enumerate(modulo_range(strip,*sec_band_pos)):
            strip.setPixelColor(pos, sec_colors[ind])
        
        strip.show()
        time.sleep(wait_ms / 1000.0)

        iterations -= 1
