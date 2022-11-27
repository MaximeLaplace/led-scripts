import sys

sys.path.insert(0, "/var/www/led-app/led-scripts")

activate = "/Documents/led-scripts/.venv/bin/activate"

with open(activate) as file_:
    exec(file_.read(), dict(__file__=activate))

from app import app as application
