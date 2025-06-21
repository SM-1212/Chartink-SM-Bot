from datetime import datetime, timedelta

# Sample mock lot size database (replace with real API or dynamic data)
LOT_SIZES = {
    "RELIANCE": 250,
    "TCS": 150,
    "HDFCBANK": 550,
    "INFY": 300,
    # Add all F&O stocks here
}

def get_nearest_expiry():
    today = datetime.today()
    weekday = today.weekday()
    days_to_thursday = (3 - weekday + 7) % 7 or 7
    expiry = today + timedelta(days=days_to_thursday)
    return expiry.strftime("%Y-%m-%d")

def select_option_contract(stock, opt_type):
    try:
        lot = LOT_SIZES.get(stock.upper(), 1)
        premium = 20 if lot > 500 else 80  # Simulated logic
        strike = round(1000 + (4 * 5))  # ATM - 4 (Mocked ATM)

        full_symbol = f"{stock.upper()}_{get_nearest_expiry()}_{strike}{opt_type}"

        return {
            "stock": stock,
            "full_symbol": full_symbol,
            "lot_size": lot,
            "premium": premium
        }
    except Exception as e:
        print(f"Error selecting option for {stock}: {e}")
        return None
