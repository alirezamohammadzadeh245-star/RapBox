from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "RapBox Bot Online ✅"

@app.route("/webhook", methods=["POST"])
def webhook():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
