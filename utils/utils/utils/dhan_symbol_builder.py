import datetime
import requests

def get_next_expiry():
    # Weekly expiry is Thursday. If today is Thursday and market open, use today.
    today = datetime.date.today()
    weekday = today.weekday()

    days_ahead = 3 - weekday  # 3 = Thursday
    if days_ahead < 0:
        days_ahead += 7

    expiry = today + datetime.timedelta(days=days_ahead)
    return expiry.strftime("%d%b%y").upper()  # e.g., 27JUN24

def build_dhan_option_symbol(stock_symbol, strike_price, option_type):
    expiry = get_next_expiry()
    return f"{stock_symbol}{expiry}{strike_price}{option_type}"
