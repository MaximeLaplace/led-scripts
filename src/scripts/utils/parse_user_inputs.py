from typing import Callable, Union

from .create_inquirers import get_function_parameters, get_tuple_types


def parse_input(_input, _type):
    if _type == int:
        return int(_input)
    elif _type == float:
        return float(_input.replace(",", "."))
    elif _type() == tuple():
        tuple_types = get_tuple_types(_type)
        return tuple(
            [
                int(v) if t == "int" else v
                for v, t in zip(_input.split(","), tuple_types)
            ]
        )


def parse_user_inputs(
    function: Callable, user_inputs: dict[str, str]
) -> dict[str, Union[str, int, tuple]]:
    function_parameters = get_function_parameters(function)[1:]

    parsed_inputs = dict(user_inputs)

    for user_input, (param_name, param_type) in zip(
        user_inputs.values(), function_parameters
    ):
        parsed_inputs[param_name] = parse_input(user_input, param_type)

    return parsed_inputs
