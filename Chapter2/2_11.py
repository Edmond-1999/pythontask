fiveDigitNumber = int(input("Enter a five-digit integer: "))

digit1 = fiveDigitNumber // 10000
digit2 = (fiveDigitNumber % 10000) // 1000
digit3 = (fiveDigitNumber % 1000) // 100
digit4 = (fiveDigitNumber % 100) // 10
digit5 = fiveDigitNumber % 10

print(digit1, digit2, digit3, digit4, digit5)
