from typing import Optional

import inquirer
from config import (
    LED_BRIGHTNESS,
    LED_CHANNEL,
    LED_COUNT,
    LED_DMA,
    LED_FREQ_HZ,
    LED_INVERT,
    LED_PIN,
)
from rpi_ws281x import PixelStrip


class PixelSegment:
    def __init__(self, strip, start: int, end: int):
        self._strip = strip
        self._start = start
        self._end = end

    def numPixels(self):
        return self._end - self._start

    def setPixelColor(self, index: int, color):
        self._strip.setPixelColor(index + self._start, color)

    def setColor(self, color):
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)


class PixelStripWithSegments(PixelStrip):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self._bp = [0, 13, 50, 72, 75, 78, 115, 136, 149]

        self.segments = [
            PixelSegment(super(), self._bp[0], self._bp[1]),
            PixelSegment(super(), self._bp[1], self._bp[2]),
            PixelSegment(super(), self._bp[2], self._bp[3]),
            PixelSegment(super(), self._bp[3], self._bp[4]),
            PixelSegment(super(), self._bp[4], self._bp[5]),
            PixelSegment(super(), self._bp[5], self._bp[6]),
            PixelSegment(super(), self._bp[6], self._bp[7]),
            PixelSegment(super(), self._bp[7], self._bp[8]),
        ]

    def get_segment_from_index(self, index: int):
        segment_index = -1
        while index >= self._bp[segment_index + 1]:
            segment_index += 1
        return segment_index

    def setColor(self, color):
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)


class PixelStripSelected(PixelStripWithSegments):
    def __init__(self, segments: tuple[int], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._segments = sorted(list(set(segments)))

    def numPixels(self):
        return sum(
            [
                self.segments[segment_number].numPixels()
                for segment_number in self._segments
            ]
        )

    def _get_real_segment_from_index(self, index):
        segment_number = -1
        number_of_led = 0
        while index >= number_of_led:
            segment_number += 1
            number_of_led += self.segments[segment_number].numPixels()

        return self._segments[segment_number]

    def _transform_index(self, index):
        transformed_index = index
        segment_number = self._get_real_segment_from_index(index)
        for i in range(segment_number):
            if i not in self._segments:
                transformed_index += self.segments[i].numPixels()

    def setPixelColor(self, index: int):
        super().setPixelColor(self._transform_index(index))


def _generate_strip(segments: Optional[tuple[int]] = None):
    if segments is not None:
        strip = PixelStripSelected(
            segments,
            LED_COUNT,
            LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            LED_BRIGHTNESS,
            LED_CHANNEL,
        )
    else:
        strip = PixelStripWithSegments(
            LED_COUNT,
            LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            LED_BRIGHTNESS,
            LED_CHANNEL,
        )

    strip.begin()
    return strip


_UPPER_LED = "Uniquement le carré de LED du haut"
_ALL_LED = "Toutes les LED"
_CUSTOM_LED = "Custom"


def create_strip():
    questions = [
        inquirer.List(
            "strip_type",
            message="Quelles LED voulez vous utiliser ?",
            choices=[
                _UPPER_LED,
                _ALL_LED,
            ],
            carousel=True,
        )
    ]
    led_to_address = inquirer.prompt(questions)["strip_type"]

    if led_to_address == _ALL_LED:
        return _generate_strip()

    if led_to_address == _UPPER_LED:
        return _generate_strip((1, 2, 5, 6))
