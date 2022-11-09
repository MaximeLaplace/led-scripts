from typing import Callable, Union

from .create_inquirers import get_function_parameters, get_tuple_types


def parse_user_inputs(
    function: Callable, user_inputs: dict[str, str]
) -> dict[str, Union[str, int, tuple]]:
    function_parameters = get_function_parameters(function)[1:]

    parsed_inputs = dict(user_inputs)

    for user_input, (param_name, param_type) in zip(
        user_inputs.values(), function_parameters
    ):
        if param_type == int:
            parsed_inputs[param_name] = int(user_input)
        elif param_type == float:
            parsed_inputs[param_name] = float(user_input.replace(",", "."))
        elif param_type() == tuple():
            tuple_types = get_tuple_types(param_type)
            parsed_inputs[param_name] = tuple(
                [
                    int(v) if t == "int" else v
                    for v, t in zip(user_input.split(","), tuple_types)
                ]
            )

    return parsed_inputs
