import argparse

from config import (
    LED_BRIGHTNESS,
    LED_CHANNEL,
    LED_COUNT,
    LED_DMA,
    LED_FREQ_HZ,
    LED_INVERT,
    LED_PIN,
)
from src.modes.utils.reset_strip import reset_strip
from src.scripts.create_strip import create_strip
from src.scripts.menu_selection import menu
from src.scripts.utils.new_terminal_section import new_terminal_section

if __name__ == "__main__":
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--clear", action="store_true", help="clear the display on exit"
    )
    script_args = parser.parse_args()

    new_terminal_section("Appli   LED")

    strip = create_strip()

    mode, args = menu()

    try:
        mode(strip, *args)

    except KeyboardInterrupt:
        if script_args.clear:
            reset_strip(strip)

    if script_args.clear:
        reset_strip(strip)
