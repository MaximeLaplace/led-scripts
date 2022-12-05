from flask import Response

from .modes_controller import modes, modes_process, reload_modes_process


def get_modes():
    return list(modes.keys())


def start_mode_controller(mode: str):
    global modes_process

    reload_modes_process(mode)

    response = Response()

    @response.call_on_close
    def on_close(process=modes_process):
        print("starting mode with mode : ", mode)
        if not process.is_alive():
            process.start()
            process.join()

    return response
