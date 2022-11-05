import os
from typing import Callable

import inquirer
from src.scripts.utils.create_inquirers import create_inquirers
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

    question_script = [
        inquirer.List(
            "script",
            message="Quel script lancer ?",
            choices=list(modes.keys()),
            carousel=True,
        )
    ]
    user_inputs = inquirer.prompt(question_script)

    mode = modes[user_inputs["script"]]

    if mode.__doc__ is not None:
        print()
        print(mode.__doc__)
        print()

    questions_mode = create_inquirers(mode)

    user_inputs = inquirer.prompt(questions_mode)
    parsed_inputs = parse_user_inputs(mode, user_inputs)

    args = parsed_inputs.values()

    return mode, args
