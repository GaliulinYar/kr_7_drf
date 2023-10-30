import requests

TOKEN = "6949650386:AAEDL0xtb5r0aM4Rd4hd-YfuQEHKpcxh9DE"


def handle(message):    # функция отправки собщения в чат
    chat_id = "476890564"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()  # Эта строка отсылает сообщение
