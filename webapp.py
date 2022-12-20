import server.src.globals as globals_
from server.app import app

application = app

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True)
