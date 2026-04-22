binary_value = input("Enter a binary number: ")

decimal_value = 0
power_value = 0

for digit in reversed(binary_value):
    decimal_value += int(digit) * (2 ** power_value)
    power_value += 1

print("Decimal equivalent:", decimal_value)
