import time

from rpi_ws281x import Color

from .utils.init_time import init_time

from random import randint


def impact(
    strip,
    color: tuple[int, int, int] = (255, 0, 0),
    impact_size: int = 3,
    fade_periods: int = 20,
    new_each: int = 3,
    wait_ms: int = 20,
    color_mode: str = "random",
    min_speed: int = 1,
    max_speed: int = 1,
    duration_s: int = 60,
    infinite: bool = True,
):
    """Créée des impacts qui disparaissent petit à petit

    Args:
        color (tuple[int, int, int]) : couleur utilisée si le color_mode vaut "color"
        impact_size (int): nombre de leds par impact = 2*impact_size + 1
        fade_periods (int) : nombre de periodes nécessaires pour faire disparaitre un impact
        new_each (int) : nombre de périodes avant chaque nouvel impact
        wait_ms (int): durée d'une période
        color_mode (str): "random" pour avoir des couleurs aléatoire, "color" pour avoir la couleur de color
        min_speed (int) : vitess minimale des impacts
        max_speed (int) : vitesse maximale des impacts
        duration_s (int): durée du mode
        infinite (bool): run le script à l'infini
    """

    time_left = init_time(duration_s)
    num_pixels = strip.numPixels()
    active_impacts = [([], color)] * fade_periods
    periods_to_new = 0

    while time_left() > 0 or infinite:
        if color_mode == "random":
            color = (randint(0, 255), randint(0, 255), randint(0, 255))

        speed = randint(min_speed, max_speed)

        active_impacts.pop(0)

        if periods_to_new == 0:
            center = randint(0, num_pixels - 1)
            impact_zone = []
            if center - impact_size >= 0:
                impact_zone.extend([i for i in range(center - impact_size, center)])
            else:
                impact_zone.extend(
                    [i for i in range(num_pixels + center - impact_size, num_pixels)]
                )
                impact_zone.extend([i for i in range(0, center)])
            impact_zone.append(center)
            if center + impact_size < num_pixels:
                impact_zone.extend(
                    [i for i in range(center + 1, center + impact_size + 1)]
                )
            else:
                impact_zone.extend([i for i in range(center + 1, num_pixels)])
                impact_zone.extend(
                    [i for i in range(0, center + impact_size + 1 - num_pixels)]
                )
            active_impacts.append((impact_zone, color, speed))
            periods_to_new = new_each - 1
        else:
            active_impacts.append(([], color, speed))
            periods_to_new -= 1

        for i in range(fade_periods):
            for j in range(len(active_impacts[i][0])):
                active_impacts[i][0][j] += active_impacts[i][2]
                active_impacts[i][0][j] %= num_pixels

        for i in range(fade_periods):
            for j in active_impacts[i][0]:
                strip.setPixelColor(
                    j, tone_down_color(active_impacts[i][1], i + 1, fade_periods)
                )

        strip.show()
        time.sleep(wait_ms / 1000)
        strip.reset()


def tone_down_color(color: tuple[int, int, int], numerator: int, denominator: int):
    return Color(
        color[0] * numerator // denominator,
        color[1] * numerator // denominator,
        color[2] * numerator // denominator,
    )
