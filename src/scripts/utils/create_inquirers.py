import re
from inspect import signature
from typing import Callable, Union

import inquirer

REGEX_BITS = {"int": "\d+", "str": ".+"}
INT_REGEX_BIT = "\d+"

NOT_EMPTY_INT_REGEX = re.compile("^\d+$")
NOT_EMPTY_STR_REGEX = re.compile("^.+$")

INQUIRERS = {
    str: lambda name: inquirer.Text(
        name,
        message=f"Specify {name} (str)",
        validate=lambda _, x: NOT_EMPTY_STR_REGEX.match(x),
    ),
    int: lambda name: inquirer.Text(
        name,
        message=f"Specify {name} (int)",
        validate=lambda _, x: NOT_EMPTY_INT_REGEX.match(x),
    ),
    bool: lambda name: inquirer.Confirm(name, message=f"{name} ?"),
    tuple(): lambda name, tuple_types: inquirer.Text(
        name,
        message=f"Specify {name} (format : {','.join(tuple_types)})",
        validate=lambda _, x: re.match(
            f"^{','.join([REGEX_BITS[t] for t in tuple_types])}$", x
        ),
    ),
}

Inquirer = Union[type(inquirer.Confirm), type(inquirer.Text)]


def get_tuple_types(tuple: type) -> list[str]:
    return [s.strip() for s in str(tuple).split("[")[1][:-1].split(",")]


def _create_inquirer(name: str, type_: Union[tuple, type]) -> Inquirer:
    if type_ in INQUIRERS:
        return INQUIRERS[type_](name)

    elif type_() in INQUIRERS:
        return INQUIRERS[type_()](name, get_tuple_types(type_))

    raise (
        TypeError(
            f"type {type_} for parameter {name} is unsupported by the inquirer generator"
        )
    )


def get_function_parameters(function: Callable[..., None]) -> list[tuple[str, type]]:
    return [
        (name, type_.annotation)
        for name, type_ in list(dict(signature(function).parameters).items())
    ]


def create_inquirers(function: Callable[..., None]) -> list[Inquirer]:
    """Takes a function and returns a list of inquirers according to its parameters"""
    inquirers = []

    for name, type_ in get_function_parameters(function)[1:]:
        inquirer = _create_inquirer(name, type_)
        if inquirer:
            inquirers.append(inquirer)

    return inquirers
