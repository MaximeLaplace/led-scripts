import server.src.globals as globals_
from server.app import app

application = app

if __name__ == "__main__":
    try:
        application.run(debug=True, use_reloader=True)

    except KeyboardInterrupt:
        globals_.modes_process.kill()
