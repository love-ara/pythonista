def calculate_payment(successful_deliveries) -> int:
    if successful_deliveries <= 0:
        raise ValueError("Successful deliveries cannot be negative")
    elif successful_deliveries > 100:
        raise ValueError("Successful deliveries cannot be more than 100")

    base_pay = 5000

    if successful_deliveries < 50:
        wage = successful_deliveries * 160
    elif 50 <= successful_deliveries < 60:
        wage = successful_deliveries * 200
    elif 60 <= successful_deliveries < 70:
        wage = successful_deliveries * 250
    else:
        wage = successful_deliveries * 500

    return wage + base_pay


