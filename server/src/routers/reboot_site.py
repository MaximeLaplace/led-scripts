from flask import Blueprint, request

from server.src.controllers.reboot_site_controller import (
    reboot_site_controller,
)

reboot_site_bp = Blueprint("reboot_site_bp", __name__)


@reboot_site_bp.route("/reboot_site", methods=["POST"])
def reboot_site():
    password = request.get_json(silent=True)["password"]

    return reboot_site_controller(password)
