five_digit_number = int(input("Enter a five-digit integer: "))

digit_1 = five_digit_number // 10000
digit_2 = (five_digit_number % 10000) // 1000
digit_3 = (five_digit_number % 1000) // 100
digit_4 = (five_digit_number % 100) // 10
digit_5 = five_digit_number % 10

print(digit_1, digit_2, digit_3, digit_4, digit_5)