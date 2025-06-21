import random

# Dummy premium simulator for test mode
def fetch_dummy_premium(symbol, option_type, strike_price):
    # Simulate premiums between ₹8 to ₹90 depending on the symbol
    return round(random.uniform(8, 90), 2)

def select_option(stock_symbol, option_type):
    try:
        # Simulate ATM strike price
        atm_strike = random.randrange(100, 2000, 10)
        far_atm_strike = atm_strike - 4 * 10  # ATM - 4 strikes

        option_symbol = f"{stock_symbol}{far_atm_strike}{option_type}"
        premium = fetch_dummy_premium(stock_symbol, option_type, far_atm_strike)

        return {
            "option_symbol": option_symbol,
            "strike_price": far_atm_strike,
            "premium": premium
        }

    except Exception as e:
        print(f"⚠️ Error selecting option for {stock_symbol}: {e}")
        return None
