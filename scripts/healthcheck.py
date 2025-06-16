import requests
import sys

def healthcheck(url):
    try:
        response = requests.get(url, timeout=20)
        if response.status_code == 200:
            print(f"✅ Healthcheck OK - {url}")
            sys.exit(0)
        else:
            print(f"❌ Healthcheck FAILED - Status code: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Healthcheck ERROR - {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python healthcheck.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    healthcheck(url)
