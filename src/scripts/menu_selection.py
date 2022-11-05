import os
from typing import Callable

import inquirer
import pyfiglet
from src.scripts.utils.create_inquirers import create_inquirers, get_function_parameters
from src.scripts.utils.parse_user_inputs import parse_user_inputs

before = globals().copy()
from src.modes import *

after = globals().copy()

modes = {}
for key, value in after.items():
    if (
        key not in before.keys()
        and key != "before"
        and type(value).__name__ != "module"
    ):
        modes[key] = after[key]


def menu() -> tuple[Callable[..., None], list[str]]:
    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format("Appli    LED"))
    print()

    question_mode = [
        inquirer.List(
            "mode",
            message="Quel mode lancer ?",
            choices=list(modes.keys()),
            carousel=True,
        )
    ]
    user_inputs = inquirer.prompt(question_mode)

    mode = modes[user_inputs["mode"]]

    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format(user_inputs["mode"].replace("_", "  ")))
    print()

    if mode.__doc__ is not None:
        print(mode.__doc__)
        print()

    use_default_values = False
    if mode.__defaults__ is not None:
        print("Des valeurs par défaut existent :")

        mode_params = get_function_parameters(mode)
        for (argname, _), default_value in zip(
            mode_params[len(mode_params) - len(mode.__defaults__) :], mode.__defaults__
        ):
            print(f"   {argname} : {default_value}")
        print()
        use_default_values = inquirer.prompt(
            [
                inquirer.Confirm(
                    "default", message="Voulez-vous les utiliser ?", default=True
                )
            ]
        )["default"]
        print()

    questions_mode = create_inquirers(mode, use_default_values=use_default_values)

    user_inputs = inquirer.prompt(questions_mode)
    parsed_inputs = parse_user_inputs(mode, user_inputs)

    args = parsed_inputs.values()

    return mode, args
