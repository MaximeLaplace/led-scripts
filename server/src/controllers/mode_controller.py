import inspect
from typing import Callable, Union

from .modes_controller import modes


def get_function_parameters(function: Callable[..., None]) -> list[tuple[str, type]]:
    args = list(inspect.signature(function).parameters.keys())
    args_values = list(inspect.signature(function).parameters.values())
    for arg in args_values:
        if arg.default is arg.empty:
            args.pop(0)

    defaults = [
        arg_value.default for arg_value in args_values[len(args_values) - len(args) :]
    ]

    params = {name: default for [name, default] in zip(args, defaults)}

    return params


def get_mode_parameters(mode: str):
    return get_function_parameters(modes[mode])
