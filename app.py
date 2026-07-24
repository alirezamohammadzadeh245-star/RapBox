from flask import Flask
import requests
from config import RUBIKA_TOKEN
from routes import setup_routes

app = Flask(__name__)

# ثبت Routeهای اصلی
setup_routes(app)


@app.route("/")
def home():
    return "RapBox Bot Online ✅"


# برای تست اینکه Render درست کار می‌کند
@app.route("/test")
def test():
    return "OK"


# ثبت Webhook در روبیکا
@app.route("/setendpoint")
def set_endpoint():

    endpoint_url = "https://rapbox-1.onrender.com/webhook"

    api_url = f"https://botapi.rubika.ir/v3/{RUBIKA_TOKEN}/updateBotEndpoints"

    payload = {
        "url": endpoint_url,
        "type": "ReceiveUpdate"
    }

    try:
        response = requests.post(
            api_url,
            json=payload,
            timeout=10
        )

        return {
            "rubika_response": response.text,
            "sent_type": "ReceiveUpdate",
            "sent_url": endpoint_url
        }

    except Exception as e:
        return {
            "error": str(e)
        }, 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
