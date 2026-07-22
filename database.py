import json
import os

FILE = "songs.json"


def load_data():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_song(song_id, file_id):
    data = load_data()
    data[song_id] = {
        "file_id": file_id,
        "downloads": 0,
        "users": []
    }
    save_data(data)


def get_song(song_id):
    data = load_data()
    return data.get(song_id)


def increase_download(song_id, user_id):
    data = load_data()

    if song_id in data:
        data[song_id]["downloads"] += 1

        if user_id not in data[song_id]["users"]:
            data[song_id]["users"].append(user_id)

        save_data(data)
