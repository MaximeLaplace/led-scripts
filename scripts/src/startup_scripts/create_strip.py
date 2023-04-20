import inquirer

from config import (
    BREAKPOINTS,
    KANOPEE_BREAKPOINTS,
    CADRE_BREAKPOINTS,
    TAILLE_BUFFER_KANOPEE,
    LED_BRIGHTNESS,
    LED_CHANNEL,
    LED_COUNT,
    LED_DMA,
    LED_FREQ_HZ,
    LED_INVERT,
    LED_PIN,
)
from rpi_ws281x import PixelStrip

from .utils.create_inquirers import INQUIRERS


class PixelSegment:
    def __init__(self, strip, start: int, end: int):
        self._strip = strip
        self._start = start
        self._end = end
        self._colors = [0 for i in range(start, end)]

    def numPixels(self):
        return self._end - self._start

    def getColors(self):
        return [color for color in self]

    def setPixelColor(self, index: int, color):
        self._colors[index] = color
        self._strip.setPixelColor(index + self._start, color)

    def setColor(self, color):
        self._colors = [color for i in range(self.numPixels())]
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)

    def setArrayColor(self, color_array):
        if self.numPixels() != len(color_array):
            raise (
                ValueError(
                    f"L'array de couleur n'a pas autant de couleurs ({len(color_array)} couleurs) qu'il y a de LED sur la bande ({self.numPixels()} LEDs) !"
                )
            )
        for i in range(self.numPixels()):
            self._colors[i] = color_array[i]
            self.setPixelColor(i, color_array[i])

    def shiftColors(self, direction: int = 1):
        if direction == -1:
            self._colors.append(self._colors.pop(0))
        else:
            self._colors.insert(0, self._colors.pop(-1))

        self.setArrayColor(self._colors)

class PixelStripWithSegments(PixelStrip):
    def __init__(self, breakpoints=BREAKPOINTS,*args, **kwargs):
        super().__init__(*args, *kwargs)

        self.breakpoints = breakpoints
        self.segments = []
        for i in range(len(breakpoints)-1):
            self.segments.append(PixelSegment(super(), breakpoints[i], breakpoints[i+1]))

    def get_segment_from_index(self, index: int):
        segment_index = -1
        while index >= self.breakpoints[segment_index + 1]:
            segment_index += 1
        return segment_index

    def setColor(self, color):
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)

    def reset(self):
        for i in range(self.numPixels()):
            self.setPixelColor(i, 0)


class PixelStripSelected(PixelStripWithSegments):
    def __init__(self, segments: tuple[int], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._segments = sorted(list(set(segments)))
        self.mode_segments = [self.segments[index] for index in self._segments]

    def numPixels(self):
        return sum(
            [
                self.segments[segment_number].numPixels()
                for segment_number in self._segments
            ]
        )

    def _get_real_segment_number_from_index(self, index):
        segment_number = -1
        number_of_led = 0
        while index >= number_of_led:
            segment_number += 1
            number_of_led += self.mode_segments[segment_number].numPixels()
        return self._segments[segment_number]

    def _transform_index(self, index):
        transformed_index = index
        segment_number = self._get_real_segment_number_from_index(index)
        for i in range(segment_number):
            if i not in self._segments:
                transformed_index += self.segments[i].numPixels()
        return transformed_index

    def setPixelColor(self, index: int, color):
        super().setPixelColor(self._transform_index(index), color)

    def setArrayColor(self, color_array):
        if self.numPixels() != len(color_array):
            raise (
                ValueError(
                    f"L'array de couleur n'a pas autant de couleurs ({len(color_array)} couleurs) qu'il y a de LED sur la bande ({self.numPixels()} LEDs) !"
                )
            )
        for i in range(self.numPixels()):
            self.setPixelColor(i, color_array[i])


def _generate_strip(segments: tuple[int] = (0, 1, 2, 3, 4, 5, 6, 7)):
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

    strip.begin()
    return strip

def _generate_kanopee_strip():
    segments_lettres = (1, 3, 5, 7, 9, 11, 13, 15, 17)

    strip = PixelStripSelected(
        segments_lettres,
        KANOPEE_BREAKPOINTS,
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL
    )
    strip.begin()
    return strip

def _generate_kanopee_cadre_strip():
    new_breakpoints = CADRE_BREAKPOINTS
    new_breakpoints.extend([p + CADRE_BREAKPOINTS[-1] - (13 - TAILLE_BUFFER_KANOPEE) for p in KANOPEE_BREAKPOINTS[1:]])

    segments_interessants = (0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

    strip = PixelStripSelected(
        segments_interessants,
        new_breakpoints,
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL
    )
    strip.begin()
    return strip

UPPER_LED = "Uniquement le carré de LED du haut"
ALL_LED = "Toutes les LED"
_CUSTOM_LED = "Custom"
KANOPEE = "Kanopée"
KANOPEE_CADRE = "Kanopée avec cadre"


def create_strip(choice: str = None):
    led_to_address = ""

    if choice is None:
        questions = [
            inquirer.List(
                "strip_type",
                message="Quelles LED voulez vous utiliser ?",
                choices=[ALL_LED, UPPER_LED, KANOPEE, KANOPEE_CADRE, _CUSTOM_LED],
                carousel=True,
            )
        ]
        led_to_address = inquirer.prompt(questions)["strip_type"]
    else:
        led_to_address = choice

    if led_to_address == ALL_LED:
        return _generate_strip()

    if led_to_address == UPPER_LED:
        return _generate_strip((1, 2, 5, 6))
    
    if led_to_address == KANOPEE:
        return _generate_kanopee_strip()
    
    if led_to_address == KANOPEE_CADRE:
        return _generate_kanopee_cadre_strip()

    if led_to_address == _CUSTOM_LED:
        segments = inquirer.prompt(
            [
                inquirer.Checkbox(
                    "segments",
                    message="Sélectionnez les segments désirés",
                    choices=[0, 1, 2, 3, 4, 5, 6, 7],
                    carousel=True,
                )
            ]
        )["segments"]

        return _generate_strip(tuple(segments))

    return _generate_strip()
