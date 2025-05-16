import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    print("📨 Sending to Telegram...")

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Telegram credentials missing.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=data)
        print(f"📡 Telegram response: {response.status_code} - {response.text}")
        if response.status_code != 200:
            print(f"❌ Telegram error: {response.text}")
        else:
            print("✅ Message sent to Telegram.")

    except Exception as e:
        print(f"❌ Exception sending message: {e}")
