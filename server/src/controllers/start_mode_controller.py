from flask import Response

import server.src.globals as globals_

from .modes_controller import modes, reload_modes_process

FAVORITES = [
    "blackout",
    "bogo_continuous",
    "bouncing_pulse",
    "christmas",
    "color_wipe_blue",
    "color_wipe_green",
    "color_wipe_red",
    "gradient_blink",
    "pulse",
    "rainbow",
    "segment_strobo",
    "slider_strobo",
    "strobo",
    "theater_chase_blue",
    "theater_chase_green",
    "theater_chase_red",
]


def get_modes():
    return list(modes.keys())


def get_favorite_modes():
    return FAVORITES


def start_mode_controller(mode: str):
    reload_modes_process(mode)

    response = Response()

    @response.call_on_close
    def on_close(process=globals_.modes_process):
        if not process.is_alive():
            process.start()
            process.join()

    return response
