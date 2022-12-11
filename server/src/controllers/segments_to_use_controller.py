import server.src.globals as globals_
from scripts.src.startup_scripts.create_strip import ALL_LED, UPPER_LED

from .start_mode_controller import start_mode_controller


def update_segments_to_use_controller(segments_to_use: str):
    if segments_to_use not in ("all", "top"):
        return "Invalid segments to use", 400

    if segments_to_use == "top":
        globals_.segments_to_use = UPPER_LED
    if segments_to_use == "all":
        globals_.segments_to_use = ALL_LED

    if globals_.current_mode is not None:
        return start_mode_controller(globals_.current_mode)

    return "Updated", 200
