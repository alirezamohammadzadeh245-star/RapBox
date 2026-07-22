from config import ADMIN_ID
from database import add_song, load_data


def is_admin(user_id):
    return str(user_id) == str(ADMIN_ID)


def add_new_song(song_id, file_id):
    add_song(song_id, file_id)


def get_stats():
    data = load_data()

    total_downloads = 0
    total_users = 0

    for song in data.values():
        total_downloads += song.get("downloads", 0)
        total_users += len(song.get("users", []))

    return {
        "songs": len(data),
        "downloads": total_downloads,
        "users": total_users
    }
