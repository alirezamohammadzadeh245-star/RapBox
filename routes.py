from flask import request, jsonify
from rubika import send_message


def setup_routes(app):

    @app.route("/webhook", methods=["POST"])
    def webhook():
        data = request.json

        try:
            update = data["update"]

            if update["type"] == "NewMessage":
                chat_id = update["chat_id"]
                text = update["new_message"].get("text", "")

                send_message(
                    chat_id,
                    "سلام 👋\nآهنگ استوری شما آماده ارسال است 🎧"
                )

        except Exception as e:
            print(e)

        return jsonify({"status": "ok"})


    @app.route("/")
    def home():
        return "RapBox Bot Online ✅"
