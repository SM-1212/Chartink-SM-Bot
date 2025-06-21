import os
import requests
from dotenv import load_dotenv

load_dotenv()

DHAN_CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

BASE_URL = "https://api.dhan.co"

HEADERS = {
    "access-token": DHAN_ACCESS_TOKEN,
    "Content-Type": "application/json",
    "client-id": DHAN_CLIENT_ID
}

def place_dhan_order(symbol, side, qty, sl_points, tsl_points):
    try:
        payload = {
            "securityId": symbol,
            "transactionType": "BUY" if side == "BUY" else "SELL",
            "exchangeSegment": "NFO",
            "orderType": "MARKET",
            "productType": "DELIVERY",  # Ensure delivery trade
            "quantity": qty,
            "afterMarketOrder": False,
            "amoTime": "",
            "disclosedQuantity": 0,
            "orderValidity": "DAY",
            "price": 0,
            "triggerPrice": 0,
            "orderSource": "API",
            "stopLoss": sl_points,
            "trailingStopLoss": tsl_points
        }

        response = requests.post(
            f"{BASE_URL}/orders",
            headers=HEADERS,
            json=payload
        )

        if response.status_code == 200:
            print(f"✅ Order placed: {symbol} | Qty: {qty} | SL: {sl_points} | TSL: {tsl_points}")
        else:
            print(f"❌ Order failed: {response.status_code} → {response.text}")

    except Exception as e:
        print(f"⚠️ Error placing order: {e}")
