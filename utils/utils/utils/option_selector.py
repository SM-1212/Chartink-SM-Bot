import math
import requests
from utils.dhan_symbol_builder import build_dhan_option_symbol

# NSE lot sizes (as per June 2025)
LOT_SIZES = {
    "RELIANCE": 250,
    "HDFCBANK": 550,
    "INFY": 300,
    "ICICIBANK": 675,
    "TCS": 150,
    "ITC": 3200,
    "AXISBANK": 675,
    "LT": 300,
    "SBIN": 1500,
    "KOTAKBANK": 400,
    "COFORGE": 100,
    "PERSISTENT": 150,
    "ZEEL": 3000,
    # Add all other F&O symbols here...
}

def get_ltp(symbol):
    url = f"https://api.dhan.co/quotes/nse/cash/{symbol}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return float(data.get("lastTradedPrice", 0))
    except Exception as e:
        print(f"⚠️ Failed to fetch LTP for {symbol}: {e}")
    return None

def get_nearest_strike(ltp):
    return int(round(ltp / 10.0) * 10)

def select_option_contract(stock_symbol, option_type):
    ltp = get_ltp(stock_symbol)
    if not ltp or ltp <= 0:
        print(f"⚠️ Invalid LTP for {stock_symbol}")
        return None

    atm_strike = get_nearest_strike(ltp)
    far_strike = atm_strike - 40  # ATM - 4 strikes

    full_symbol = build_dhan_option_symbol(stock_symbol, far_strike, option_type)
    lot_size = LOT_SIZES.get(stock_symbol.upper(), 100)  # Default fallback

    # Simulated premium for SL/TSL logic (real premium fetch optional)
    premium = round(far_strike * 0.03, 2)

    return {
        "full_symbol": full_symbol,
        "strike_price": far_strike,
        "premium": premium,
        "lot_size": lot_size
    }
