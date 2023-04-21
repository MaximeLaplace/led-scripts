import server.src.globals as globals_
from scripts.src.startup_scripts.create_strip import (
    ALL_LED,
    KANOPEE,
    KANOPEE_CADRE,
    UPPER_LED,
)

from .start_mode_controller import start_mode_controller

_FRONT_TO_BACK = {
    "top": UPPER_LED,
    "all": ALL_LED,
    "kano": KANOPEE,
    "kano_c": KANOPEE_CADRE,
}
_BACK_TO_FRONT = {
    UPPER_LED: "top",
    ALL_LED: "all",
    KANOPEE: "kano",
    KANOPEE_CADRE: "kano_c",
}


def get_segments_to_use():
    return _BACK_TO_FRONT[globals_.segments_to_use]


def update_segments_to_use_controller(segments_to_use: str):
    if segments_to_use not in ("all", "top", "kano", "kano_c"):
        return "Invalid segments to use", 400

    globals_.segments_to_use = _FRONT_TO_BACK[segments_to_use]

    if globals_.current_mode is not None:
        return start_mode_controller(globals_.current_mode)

    return "Updated", 200
