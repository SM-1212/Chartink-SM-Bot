def calculate_sl_tsl(premium):
    """
    Professional logic for SL/TSL based on option premium (strict intraday style):
    - For premium <= ₹15 → SL: 4 pts, TSL: 2 pts
    - ₹16 – ₹30 → SL: 6 pts, TSL: 3 pts
    - ₹31 – ₹60 → SL: 9 pts, TSL: 5 pts
    - ₹61 – ₹100 → SL: 13 pts, TSL: 7 pts
    - ₹100+ → SL: 15 pts, TSL: 10 pts
    """
    if premium <= 15:
        return 4, 2
    elif 15 < premium <= 30:
        return 6, 3
    elif 30 < premium <= 60:
        return 9, 5
    elif 60 < premium <= 100:
        return 13, 7
    else:
        return 15, 10
