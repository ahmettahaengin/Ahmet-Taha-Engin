import requests
TOKEN = "YOUR TELEGRAM BOT TOKEN"
chat_id = "https://t.me/+ZWW_0dOmbx02OWI0"
message = "hello from your telegram bot"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())