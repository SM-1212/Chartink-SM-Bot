def calculate_sl_tsl(premium):
    try:
        if premium <= 20:
            return 4, 2  # SL, TSL
        elif premium <= 50:
            return 8, 4
        elif premium <= 100:
            return 12, 6
        else:
            return 20, 10
    except:
        return 10, 5  # default safety fallback
