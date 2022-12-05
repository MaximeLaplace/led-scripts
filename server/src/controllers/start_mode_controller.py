from flask import Response

import server.src.globals as globals_

from .modes_controller import modes, reload_modes_process


def get_modes():
    return list(modes.keys())


def start_mode_controller(mode: str):
    reload_modes_process(mode)

    response = Response()

    @response.call_on_close
    def on_close(process=globals_.modes_process):
        print("starting mode with mode : ", mode)
        if not process.is_alive():
            process.start()
            process.join()

    return response
