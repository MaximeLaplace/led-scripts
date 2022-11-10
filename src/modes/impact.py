import time

from rpi_ws281x import Color

from .utils.init_time import init_time

from random import randint

def impact(
    strip,
    color: tuple[int, int, int] = (255, 0, 0),
    impact_size: int = 2,
    fade_periods: int = 10,
    new_each: int = 2,
    wait_ms: int = 200,
    duration_s: int = 60,
    infinite: bool = False,
):
    time_left = init_time(duration_s)
    num_pixels = strip.numPixels()
    active_impacts = [[]]*fade_periods
    periods_to_new = 0

    while time_left() > 0 or infinite:
        active_impacts.pop(0)

        if periods_to_new == 0:
            center = randint(0, num_pixels-1)
            impact_zone = []
            if center - impact_size >= 0:
                impact_zone.extend([i for i in range(center - impact_size, center)])
            else :
                impact_zone.extend([i for i in range(num_pixels + center - impact_size, num_pixels)])
                impact_zone.extend([i for i in range(0, center)])
            impact_zone.append(center)
            if center + impact_size < num_pixels:
                impact_zone.extend([i for i in range(center + 1, center + impact_size + 1)])
            else :
                impact_zone.extend([i for i in range(center +1, num_pixels)])
                impact_zone.extend([i for i in range(0, center + impact_size + 1 - num_pixels)])
            active_impacts.append(impact_zone)
            periods_to_new = new_each - 1
        else:
            active_impacts.append([])
            periods_to_new -= 1
        
        for i in range(fade_periods):
            for j in active_impacts[i]:
                strip.setPixelColor(j, tone_down_color(color, i+1, fade_periods))

        strip.show()
        time.sleep(wait_ms / 1000)
        strip.reset()

def tone_down_color(
    color: tuple[int, int, int],
    numerator: int,
    denominator: int
):
    return Color(color[0]*numerator//denominator, color[1]*numerator//denominator, color[2]*numerator//denominator)