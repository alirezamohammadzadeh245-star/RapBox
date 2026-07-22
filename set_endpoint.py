import requests
from config import RUBIKA_TOKEN

url = f"https://botapi.rubika.ir/v3/{RUBIKA_TOKEN}/updateBotEndpoint"

data = {
    "url": "https://rapbox-1.onrender.com/webhook"
}

response = requests.post(url, json=data)

print(response.text)
