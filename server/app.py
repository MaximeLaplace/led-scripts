from flask import Flask, render_template
from flask_cors import CORS
import socket
import server.src.globals as globals_
from telegrambot.send_message import send_ip

from .src.routers import segments_to_use_bp, speed_factor_bp, start_mode_bp

app = Flask(
    __name__,
    static_folder="../front/build",
    static_url_path="",
    template_folder="../front/build",
)

cors = CORS(app)

app.register_blueprint(start_mode_bp)
app.register_blueprint(segments_to_use_bp)
app.register_blueprint(speed_factor_bp)

globals_.init()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP_ADDRESS = s.getsockname()[0]
s.close()
send_ip(f"{IP_ADDRESS}:5000")


@app.route("/")
def home():
    return render_template("index.html")
