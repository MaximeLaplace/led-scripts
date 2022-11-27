import time
from random import random

from rpi_ws281x import Color


def sparkle(strip, sparkles, wait_ms: int = 50):
    steps = 10
    intensities = [int(255 / steps * i) for i in range(1, steps + 1)]
    intensities.extend(intensities[:-1][::-1])

    indices, offsets = zip(*sparkles)

    for p in intensities:
        for index in indices:
            strip.setPixelColor(index - 1, Color(int(p / 6), int(p / 6), int(p / 6)))
            strip.setPixelColor(index, Color(p, p, p))
            strip.setPixelColor(index + 1, Color(int(p / 6), int(p / 6), int(p / 6)))

        strip.show()
        time.sleep(wait_ms / 1000)
    strip.reset()
    strip.show()


def christmas(strip, wait_ms: int = 50, sparkles_number: int = 10):
    while True:
        strip.reset()
        length = strip.numPixels()
        seg = int(length / sparkles_number)

        indices = []
        for i in range(sparkles_number):
            index = int(random() * seg + seg * i)
            offset = random() * 150 / 1000
            indices.append((index, offset))

        sparkle(strip, indices, wait_ms=wait_ms)

        time.sleep(wait_ms / 1000)
