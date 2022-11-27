import json
import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

from flask import Flask

app = Flask(__name__)


@app.route("/add")
def add():
    shared_mode.add()
    return f"Home sweet home! (and {shared_mode.get()})"


@app.route("/substract")
def sub():
    shared_mode.substract()
    return f"Home sweet home! (and {shared_mode.get()})"


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


def work(shared_mode):
    while True:
        print(f"shared_modes is at list length : {shared_mode.get()}")
        time.sleep(1)


if __name__ == "__main__":
    with CustomManager() as manager:
        shared_mode = manager.Mode()

        process = Process(target=work, args=(shared_mode,))

        process.start()
        app.run(debug=True, use_reloader=False)
        process.join()
