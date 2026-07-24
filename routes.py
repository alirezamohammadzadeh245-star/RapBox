from flask import request, jsonify
from rubika import send_message


def setup_routes(app):

    @app.route("/webhook", methods=["POST"])
    def webhook():
        data = request.json

        try:
            update = data.get("update", {})

            if update.get("type") == "NewMessage":

                chat_id = update.get("chat_id")

                new_message = update.get("new_message", {})
                text = new_message.get("text", "")

                if chat_id:
                    send_message(
                        chat_id,
                        "سلام 👋\nآهنگ استوری شما آماده ارسال است 🎧"
                    )

        except Exception as e:
            print("Webhook Error:", e)

        return jsonify({"status": "ok"})
