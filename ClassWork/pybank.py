def validate_email(email):
    if "@" not in email:
        raise ValueError("Invalid Email")
    if email[0] == "@" or email[-1] == "@":
        return "invalid email"
    if len(email) >= 8:
        return True
    return False


def calculate_balance(transactions):
    total = 0
    for amount in transactions:
        total += amount
    return total
