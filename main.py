import os
from dotenv import load_dotenv
from utils.chartink_fetcher import get_chartink_stocks
from utils.option_selector import select_option_contract
from utils.sl_tsl_manager import calculate_sl_tsl
from utils.dhan_api import place_dhan_order

load_dotenv()

# Load environment variables
CALL_URL = os.getenv("CHARTINK_URL_CALL")
PUT_URL = os.getenv("CHARTINK_URL_PUT")

def execute_live_bot():
    print("🚀 Starting Chartink + Dhan Bot (LIVE Mode)\n")

    # Fetch stocks from Chartink screeners
    call_stocks = get_chartink_stocks(CALL_URL)
    put_stocks = get_chartink_stocks(PUT_URL)

    print(f"📈 CALL Candidates (Open=Low): {call_stocks}")
    print(f"📉 PUT Candidates (Open=High): {put_stocks}")

    # Process CALL trades
    for stock in call_stocks:
        option = select_option_contract(stock, "CE")
        if option:
            sl, tsl = calculate_sl_tsl(option["premium"])
            place_dhan_order(
                symbol=option["full_symbol"],
                side="BUY",
                qty=option["lot_size"],
                sl_points=sl,
                tsl_points=tsl
            )

    # Process PUT trades
    for stock in put_stocks:
        option = select_option_contract(stock, "PE")
        if option:
            sl, tsl = calculate_sl_tsl(option["premium"])
            place_dhan_order(
                symbol=option["full_symbol"],
                side="BUY",
                qty=option["lot_size"],
                sl_points=sl,
                tsl_points=tsl
            )

if __name__ == "__main__":
    execute_live_bot()
