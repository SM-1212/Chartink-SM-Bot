def calculate_sl_tsl(premium):
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