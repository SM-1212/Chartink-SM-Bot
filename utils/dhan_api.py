import os
import requests
from dotenv import load_dotenv

load_dotenv()

DHAN_CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

HEADERS = {
    "access-token": DHAN_ACCESS_TOKEN,
    "client-id": DHAN_CLIENT_ID,
    "Content-Type": "application/json"
}

def place_dhan_order(symbol, side, qty, sl_points=0, tsl_points=0):
    order_type = "LIMIT"
    product_type = "INTRADAY"
    transaction_type = side.upper()  # BUY or SELL

    body = {
        "symbol": symbol,
        "transactionType": transaction_type,
        "quantity": qty,
        "orderType": order_type,
        "productType": product_type,
        "price": 0,
        "triggerPrice": 0,
        "disclosedQuantity": 0,
        "validity": "DAY",
        "afterMarketOrder": False,
        "boProfitValue": tsl_points,
        "boStopLossValue": sl_points
    }

    try:
        response = requests.post(
            url="https://api.dhan.co/orders",
            json=body,
            headers=HEADERS
        )
        if response.status_code == 200:
            print(f"✅ Order Placed: {symbol}")
        else:
            print(f"❌ Order Failed: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"🚨 Error placing order: {e}")
