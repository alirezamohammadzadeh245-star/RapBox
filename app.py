from flask import Flask
import requests
from config import RUBIKA_TOKEN
from routes import setup_routes

app = Flask(__name__)

# ثبت route های webhook
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


@app.route("/getme")
def getme():
    url = f"https://botapi.rubika.ir/v3/{RUBIKA_TOKEN}/getMe"

    try:
        response = requests.post(
            url,
            timeout=10
        )

        return response.text

    except Exception as e:
        return str(e)


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
            "sent_url": data["url"],
            "sent_type": data["type"]
        }

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
