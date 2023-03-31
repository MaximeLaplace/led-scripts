from flask import Blueprint, request

from server.src.controllers.mode_controller import (
    get_mode_parameters as get_mode_parameters_controller,
)

mode_bp = Blueprint("mode", __name__)


@mode_bp.route("/mode-parameters", methods=["GET"])
def get_mode_parameters():
    mode = request.args.get("mode")

    return get_mode_parameters_controller(mode)


@mode_bp.route("/mode-parameters/<mode>", methods=["POST"])
def update_mode_parameters(mode):
    new_parameters = request.get_json(silent=True)

    return get_mode_parameters(mode)
