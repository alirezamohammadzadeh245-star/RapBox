from flask import Flask
from routes import setup_routes

app = Flask(__name__)

setup_routes(app)

@app.route("/")
def home():
    return "RapBox Bot Online ✅"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
