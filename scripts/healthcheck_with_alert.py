import requests
import sys
import os

# 🚨 Dados do Telegram
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"❌ Falha ao enviar alerta Telegram: {response.text}")
    except Exception as e:
        print(f"❌ Erro Telegram: {e}")

def healthcheck(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ Healthcheck OK - {url}")
            sys.exit(0)
        else:
            print(f"❌ Healthcheck FAILED - Status code: {response.status_code}")
            send_telegram_alert(f"🚨 Healthcheck FAILED: {url} Status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Healthcheck ERROR - {e}")
        send_telegram_alert(f"🚨 Healthcheck ERROR: {url} - {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python healthcheck_with_alert.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    healthcheck(url)
