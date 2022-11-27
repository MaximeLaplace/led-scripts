import sys

sys.path.insert(0, "/var/www/led-app")

activate = "/Documents/led-scripts/env/bin/activate"

with open(activate) as file_:
    exec(file_.read(), dict(__file__=activate))

from app import app as application
