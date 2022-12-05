import os

import pyfiglet


def new_terminal_section(message: str):
    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format(message))
    print()
