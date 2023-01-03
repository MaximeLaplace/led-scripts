import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP_ADDRESS = s.getsockname()[0]
s.close()

print(IP_ADDRESS)

from telegrambot.send_message import send_ip

send_ip(f"{IP_ADDRESS}:{5000}")
