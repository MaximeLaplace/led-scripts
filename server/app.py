import json
import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

from flask import Flask, Response, render_template
from flask_cors import CORS

from .src.routers.start_mode import start_mode_bp

app = Flask(
    __name__,
    static_folder="../front/build",
    static_url_path="",
    template_folder="../front/build",
)

cors = CORS(app)

app.register_blueprint(start_mode_bp)


@app.route("/")
def home():
    return render_template("index.html")


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
