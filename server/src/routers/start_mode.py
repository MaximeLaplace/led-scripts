from flask import Blueprint, request

from server.src.controllers.start_mode_controller import (
    get_modes,
    start_mode_controller,
)

start_mode_bp = Blueprint("start_mode", __name__)


@start_mode_bp.route("/start_mode", methods=["GET"])
def start_mode():
    return get_modes()


@start_mode_bp.route("/start_mode", methods=["POST"])
def start_mode_post():
    mode = request.get_json(silent=True)["mode"]

    return start_mode_controller(mode)
