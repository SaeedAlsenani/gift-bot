import requests

TOKEN = "7613654876:AAHJmkjB72I7W3GA1IcEUEQnD0fe-pNWbJ8"
URL = f"https://api.telegram.org/bot{TOKEN}/setChatMenuButton"

payload = {
    "menu_button": {
        "type": "web_app",
        "text": "مؤشر",
        "web_app": {
            "url": "https://gift-view-prices.onrender.com"
        }
    }
}

response = requests.post(URL, json=payload)
print(response.json())
