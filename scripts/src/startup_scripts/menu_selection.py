from typing import Callable

import inquirer

from .utils.create_inquirers import create_inquirers, get_function_parameters
from .utils.new_terminal_section import new_terminal_section
from .utils.parse_user_inputs import parse_user_inputs

before = globals().copy()
from scripts.src.modes import *

after = globals().copy()

modes = {}
for key, value in after.items():
    if (
        key not in before.keys()
        and key != "before"
        and type(value).__name__ != "module"
    ):
        modes[key] = after[key]

modes = dict(sorted(modes.items(), key=lambda item: item[0]))


def menu() -> tuple[Callable[..., None], list[str]]:
    new_terminal_section("Appli   LED")

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

    new_terminal_section(user_inputs["mode"].replace("_", "  "))

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
