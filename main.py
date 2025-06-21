import os, json, time
from dotenv import load_dotenv
from utils.chartink_fetcher import get_chartink_stocks
from utils.option_selector import select_option_contract
from utils.sl_tsl_manager import calculate_sl_tsl
from utils.dhan_api import place_dhan_order

# Constants
STOP_FLAG = "stop_bot.flag"
TRADE_LOG = "live_trades.json"
PNL_SUM = "pnl_summary.json"

load_dotenv()
CALL_URL = os.getenv("CHARTINK_URL_CALL")
PUT_URL = os.getenv("CHARTINK_URL_PUT")

def load_json(path, default):
    if os.path.exists(path):
        return json.load(open(path, "r"))
    with open(path, "w") as f:
        json.dump(default, f)
    return default

def save_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)

def log_trade(entry):
    trades = load_json(TRADE_LOG, [])
    trades.append(entry)
    save_json(TRADE_LOG, trades)

def update_pnl(amount):
    pnl = load_json(PNL_SUM, {"total": 0})
    pnl["total"] += amount
    save_json(PNL_SUM, pnl)

def execute_for(stock, opt_type):
    option = select_option_contract(stock, "CE" if opt_type=="CALL" else "PE")
    if not option: return

    sl, tsl = calculate_sl_tsl(option["premium"])
    symbol, qty, prem = option["full_symbol"], option["lot_size"], option["premium"]
    place_dhan_order(symbol, "BUY", qty, sl, tsl)

    entry = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stock": stock,
        "type": opt_type,
        "symbol": symbol,
        "premium": prem,
        "qty": qty,
        "sl": sl,
        "tsl": tsl,
        "status": "OPEN"
    }
    log_trade(entry)

def main():
    print("🚀 Bot started (watch dashboard for live status)…")
    # Clear previous logs
    save_json(TRADE_LOG, [])
    save_json(PNL_SUM, {"total": 0})

    while True:
        if os.path.exists(STOP_FLAG):
            print("🛑 Stop-flag detected, exiting…")
            break

        for stock in get_chartink_stocks(CALL_URL):
            execute_for(stock, "CALL")
        for stock in get_chartink_stocks(PUT_URL):
            execute_for(stock, "PUT")

        print("✅ Wait 5 min before next scan…")
        time.sleep(300)  # 5-minute interval

if __name__ == "__main__":
    main()
