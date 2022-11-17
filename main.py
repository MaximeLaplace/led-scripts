import argparse
import os

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
        os.system("cls" if os.name == "nt" else "clear")
        if script_args.clear:
            strip.reset()

    if script_args.clear:
        strip.reset()
