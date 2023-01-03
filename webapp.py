import server.src.globals as globals_
from server.app import app
from telegrambot.send_message import send_ip
import socket

application = app

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP_ADDRESS = s.getsockname()[0]
s.close()


if __name__ == "__main__":
    print("sending ip")
    send_ip(f"{IP_ADDRESS}:{5000}")
    print("ip sent")
    application.run(debug=True, use_reloader=True)
