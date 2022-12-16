import server.src.globals as globals_

from .start_mode_controller import start_mode_controller


def get_speed_factor():
    return str(globals_.speed_factor)


def _is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def update_speed_factor(speed_factor: str):
    if not _is_float(speed_factor):
        return "Invalid speed factor", 400

    if float(speed_factor) != 0:
        globals_.speed_factor = float(speed_factor)

    if globals_.current_mode is not None:
        return start_mode_controller(globals_.current_mode)

    return "Updated", 200
