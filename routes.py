from flask import request, jsonify
from database import get_song, increase_download


def setup_routes(app):

    @app.route("/song/<song_id>", methods=["GET"])
    def send_song(song_id):
        song = get_song(song_id)

        if not song:
            return "Song not found", 404

        return jsonify({
            "status": "ok",
            "file_id": song["file_id"],
            "downloads": song["downloads"]
        })


    @app.route("/webhook", methods=["POST"])
    def webhook():
        data = request.json

        return jsonify({
            "status": "received"
        })
