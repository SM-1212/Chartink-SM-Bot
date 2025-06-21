import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("DHAN_API_KEY")
ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")
CLIENT_ID = os.getenv("DHAN_CLIENT_ID")

def place_dhan_order(symbol, side, qty, sl_points, tsl_points):
    try:
        url = "https://api.dhan.co/orders"
        headers = {
            "access-token": ACCESS_TOKEN,
            "Content-Type": "application/json"
        }

        order_data = {
            "security_id": symbol,
            "transaction_type": side,
            "quantity": qty,
            "order_type": "LIMIT",
            "price": 0,
            "product": "NRML",
            "order_source": "API",
            "stop_loss": sl_points,
            "trailing_stop_loss": tsl_points,
            "client_id": CLIENT_ID
        }

        response = requests.post(url, json=order_data, headers=headers)
        print(f"📤 Dhan order response: {response.status_code} => {response.text}")

    except Exception as e:
        print(f"❌ Error placing Dhan order: {e}")
