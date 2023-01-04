import subprocess
from flask import abort
from dotenv import load_dotenv

load_dotenv()

import os

REBOOT_PASSWORD = os.getenv("REBOOT_PASSWORD")


def check_reboot_password(password: str):
    if password != REBOOT_PASSWORD:
        pass
        abort(400)


def reboot_site_controller(password):
    check_reboot_password(password)

    subprocess.run(["git", "pull"])

    return "Success", 200
