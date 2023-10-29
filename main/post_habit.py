import requests

TOKEN = "6949650386:AAEDL0xtb5r0aM4Rd4hd-YfuQEHKpcxh9DE"


def handle(message):
    chat_id = "476890564"
    # message = "Ща тебя привычками загружу"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()  # Эта строка отсылает сообщение

    # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates" # узнать данные по чату
    # print(requests.get(url).json())
