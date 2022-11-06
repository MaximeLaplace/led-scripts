import argparse

from rpi_ws281x import PixelStrip

from config import (
    LED_BRIGHTNESS,
    LED_CHANNEL,
    LED_COUNT,
    LED_DMA,
    LED_FREQ_HZ,
    LED_INVERT,
    LED_PIN,
)
from src.scripts.menu_selection import menu
from src.strip_utils.reset_strip import reset_strip

if __name__ == "__main__":
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--clear", action="store_true", help="clear the display on exit"
    )
    script_args = parser.parse_args()

    mode, args = menu()

    strip = PixelStrip(
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL,
    )
    strip.begin()

    try:
        mode(strip, *args)

    except KeyboardInterrupt:
        if script_args.clear:
            reset_strip(strip)

    if script_args.clear:
        reset_strip(strip)
