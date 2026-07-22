import requests
from config import RUBIKA_TOKEN


def send_message(user_id, text):
    url = "https://botapi.rubika.ir/v3/" + RUBIKA_TOKEN + "/sendMessage"

    data = {
        "chat_id": user_id,
        "text": text
    }

    try:
        requests.post(url, json=data)
    except Exception as e:
        print(e)


def send_file(user_id, file_id):
    url = "https://botapi.rubika.ir/v3/" + RUBIKA_TOKEN + "/sendFile"

    data = {
        "chat_id": user_id,
        "file_id": file_id
    }

    try:
        requests.post(url, json=data)
    except Exception as e:
        print(e)
