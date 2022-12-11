from flask import Blueprint, Response

from server.src.controllers.segments_to_use_controller import (
    update_segments_to_use_controller,
)

segments_to_use_bp = Blueprint("segments_to_use", __name__)


@segments_to_use_bp.route("/segments_to_use/<segments>", methods=["POST"])
def update_segments_to_use(segments):
    return update_segments_to_use_controller(segments)
