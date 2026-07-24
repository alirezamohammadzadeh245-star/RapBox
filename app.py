from flask import Flask
import requests
from config import RUBIKA_TOKEN
from routes import setup_routes

app = Flask(__name__)

setup_routes(app)


@app.route("/")
def home():
    return "RapBox Bot Online ✅"


@app.route("/setendpoint")
def set_endpoint():

    api_url = f"https://botapi.rubika.ir/v3/{RUBIKA_TOKEN}/updateBotEndpoints"

    data = {
        "url": "https://rapbox-1.onrender.com/webhook",
        "type": "ReceiveUpdate"
    }

    try:
        response = requests.post(
            api_url,
            json=data,
            headers={
                "Content-Type": "application/json"
            },
            timeout=15
        )

        return {
            "rubika_response": response.text,
            "sent_url": data["url"],
            "sent_type": data["type"]
        }

    except Exception as e:
        return {
            "error": str(e)
        }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
