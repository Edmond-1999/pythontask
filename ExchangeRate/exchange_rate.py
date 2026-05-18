def dollar_to_naira(dollar_amount):
    exchange_rate = 1550

    if type(dollar_amount) != int and type(dollar_amount) != float:
        return "Invalid input. Please enter a numeric value."

    if dollar_amount < 0:
        return "Amount cannot be negative."

    naira = dollar_amount * exchange_rate

    return round(naira, 2)
