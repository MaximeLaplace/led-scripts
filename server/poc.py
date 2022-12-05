import json
import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

from flask import Flask, Response

from src.routers.start_mode import start_mode_bp

app = Flask(__name__)
app.register_blueprint(start_mode_bp)


class Mode:
    def __init__(self) -> None:
        self.number = 0

    def toJSON(self):
        return json.dumps(self.list)

    def serialize(self):
        return self.toJSON()

    def add(self):
        self.number += 1

    def substract(self):
        self.number -= 1

    def get(self):
        return self.number


class CustomManager(BaseManager):
    pass


CustomManager.register("Mode", Mode)


def work():
    while True:
        print(f"process running")
        time.sleep(1)


def initialize_process():
    return {"is_started": False, "process": Process(target=work)}


process = Process(target=work)


@app.route("/stop")
def stop():
    global process
    s = f"process.is_alive before closing : {process.is_alive()}"

    if process.is_alive():
        process.kill()
        process = Process(target=work)

    return s


@app.route("/start")
def start():
    global process
    response = Response(f"process.is_alive before starting : {process.is_alive()}")

    @response.call_on_close
    def on_close(process=process):
        if not process.is_alive():
            process.start()
            process.join()

    return response


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
