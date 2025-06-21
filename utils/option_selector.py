def select_option_contract(stock_symbol, option_type, strike_offset):
    """
    Select a far ATM option contract (ATM - strike_offset).
    Example: If ATM = 2500 and strike_offset = 4, return 2460 strike.
    """
    try:
        # Dummy ATM value for testing; in production, fetch LTP from live NSE or Dhan
        atm_strike = 2500

        if option_type.upper() == 'CALL':
            selected_strike = atm_strike - (strike_offset * 10)
            return f"{stock_symbol}{selected_strike}CE"
        else:
            selected_strike = atm_strike - (strike_offset * 10)
            return f"{stock_symbol}{selected_strike}PE"
    except Exception as e:
        print("Error in selecting option contract:", e)
        return None
