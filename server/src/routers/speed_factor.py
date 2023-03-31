from flask import Blueprint

from server.src.controllers.speed_factor_controller import (
    get_speed_factor,
    update_speed_factor,
)

speed_factor_bp = Blueprint("speed_factor", __name__)


@speed_factor_bp.route("/speed_factor", methods=["GET"])
def speed_factor():
    return get_speed_factor()


@speed_factor_bp.route("/speed_factor/<speed_factor>", methods=["POST"])
def update_speed_factor_router(speed_factor):
    return update_speed_factor(speed_factor)
