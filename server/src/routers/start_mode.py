from flask import Blueprint, request

start_mode_bp = Blueprint("start_mode", __name__)


@start_mode_bp.route("/start_mode", methods=["GET"])
def start_mode():
    return "A"


@start_mode_bp.route("/start_mode", methods=["POST"])
def start_mode_post():
    print(request.form)
    return "post success"
