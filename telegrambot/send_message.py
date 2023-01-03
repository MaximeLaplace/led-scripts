from dotenv import load_dotenv

load_dotenv()

import os

TELEGRAM_BOT_API_TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

import requests

TELEGRAM_IDS = ["945245928", "811139650", "912534760", "1172596706"]


def _send_message(ip: str, chat_id: str):
    url_req = f"https://api.telegram.org/bot{TELEGRAM_BOT_API_TOKEN}/sendMessage?chat_id={chat_id}&text={ip}"
    results = requests.get(url_req)
    print(results.json())


def send_ip(ip: str):
    for tg_id in TELEGRAM_IDS:
        _send_message(ip, tg_id)
