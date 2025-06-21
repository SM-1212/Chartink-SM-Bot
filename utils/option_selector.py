import requests
from utils.dhan_symbol_builder import build_dhan_option_symbol

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
}

def get_ltp(symbol):
    # Dummy return for offline testing
    return 2600 if symbol == "RELIANCE" else 1400

def get_nearest_strike(ltp):
    return int(round(ltp / 10.0) * 10)

def select_option_contract(stock_symbol, option_type):
    ltp = get_ltp(stock_symbol)
    if not ltp or ltp <= 0:
        print(f"⚠️ Invalid LTP for {stock_symbol}")
        return None

    atm_strike = get_nearest_strike(ltp)
    far_strike = atm_strike - 40

    full_symbol = build_dhan_option_symbol(stock_symbol, far_strike, option_type)
    lot_size = LOT_SIZES.get(stock_symbol.upper(), 100)
    premium = round(far_strike * 0.03, 2)

    return {
        "full_symbol": full_symbol,
        "strike_price": far_strike,
        "premium": premium,
        "lot_size": lot_size
    }