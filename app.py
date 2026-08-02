from flask import Flask, request, jsonify
import requests

from config import RUBIKA_TOKEN
from routes import setup_routes

app = Flask(__name__)

# ثبت تمام Routeهای اصلی بات
setup_routes(app)


@app.route("/")
def home():
    return "RapBox Bot Online ✅"


# تست ساده برای اطمینان از اینکه Render می‌تواند
# این URL را در اختیار روبیکا قرار دهد
@app.route("/testurl", methods=["GET", "POST"])
def testurl():
    return jsonify({
        "status": "ok",
        "url": "https://rapbox-1.onrender.com/testurl"
    })


# Webhook اصلی بات
@app.route("/webhook", methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        return jsonify({
            "status": "ok",
            "message": "Webhook Online"
        })

    try:
        data = request.get_json(silent=True)

        print("=== RUBIKA WEBHOOK ===")
        print(data)

        # فعلاً فقط تأیید دریافت درخواست
        return jsonify({
            "status": "ok"
        }), 200

    except Exception as e:
        print("WEBHOOK ERROR:", str(e))

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 200


# تنظیم Endpoint روبیکا
@app.route("/setendpoint", methods=["GET"])
def set_endpoint():

    rubika_url = (
        f"https://botapi.rubika.ir/v3/"
        f"{RUBIKA_TOKEN}/updateBotEndpoints"
    )

    data = {
        "url": "https://rapbox-1.onrender.com/testurl",
        "type": "ReceiveUpdate"
    }

    try:
        response = requests.post(
            rubika_url,
            json=data,
            timeout=20
        )

        return jsonify({
            "rubika_response": response.text,
            "sent_type": "ReceiveUpdate",
            "sent_url": "https://rapbox-1.onrender.com/testurl"
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
