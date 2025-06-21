import datetime

def get_next_expiry():
    today = datetime.date.today()
    weekday = today.weekday()
    days_ahead = 3 - weekday
    if days_ahead < 0:
        days_ahead += 7
    expiry = today + datetime.timedelta(days=days_ahead)
    return expiry.strftime("%d%b%y").upper()

def build_dhan_option_symbol(stock_symbol, strike_price, option_type):
    expiry = get_next_expiry()
    return f"{stock_symbol}{expiry}{strike_price}{option_type}"