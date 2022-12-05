from flask import Flask, render_template
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
