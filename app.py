from flask import Flask
import requests

from config import RUBIKA_TOKEN
from routes import setup_routes


app = Flask(__name__)

# تمام Routeهای اصلی از routes.py
setup_routes(app)


@app.route("/")
def home():
    return "RapBox Bot Online ✅"


@app.route("/testurl")
def testurl():
    return {
        "status": "ok",
        "url": "https://rapbox-1.onrender.com/webhook"
    }


@app.route("/setendpoint")
def set_endpoint():
    url = f"https://botapi.rubika.ir/v3/{RUBIKA_TOKEN}/updateBotEndpoints"

    data = {
        "url": "https://rapbox-1.onrender.com/webhook",
        "type": "ReceiveUpdate"
    }

    try:
        response = requests.post(
            url,
            json=data,
            timeout=10
        )

        return {
            "rubika_response": response.text,
            "sent_type": "ReceiveUpdate",
            "sent_url": data["url"]
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
