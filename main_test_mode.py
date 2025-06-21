from utils.chartink_fetcher import get_chartink_stocks
from utils.option_selector import select_option
from utils.sl_tsl_manager import calculate_sl_tsl
from utils.trade_simulator import simulate_trade

# Screener URLs (replace with your own if needed)
CALL_URL = "https://chartink.com/screener/open-low-20050514"
PUT_URL = "https://chartink.com/screener/open-high-20048202"

# Simulated Entry Point
def run_test_mode():
    print("\n🔁 Running in TEST MODE - No real trades\n")

    # Step 1: Fetch screener data
    call_stocks = get_chartink_stocks(CALL_URL)
    put_stocks = get_chartink_stocks(PUT_URL)

    all_trades = []

    # Step 2: Process CALL trades (Open = Low)
    for stock in call_stocks:
        result = select_option(stock, "CE")
        if result:
            option_data = result
            sl, tsl = calculate_sl_tsl(option_data["premium"])
            simulate_trade(stock, "CALL", option_data, sl, tsl)
            all_trades.append((stock, "CALL"))

    # Step 3: Process PUT trades (Open = High)
    for stock in put_stocks:
        result = select_option(stock, "PE")
        if result:
            option_data = result
            sl, tsl = calculate_sl_tsl(option_data["premium"])
            simulate_trade(stock, "PUT", option_data, sl, tsl)
            all_trades.append((stock, "PUT"))

    print(f"\n✅ Simulated Trades: {len(all_trades)}")
    for stock, ttype in all_trades:
        print(f"- {stock} → {ttype}")

if __name__ == "__main__":
    run_test_mode()


