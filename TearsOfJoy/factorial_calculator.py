number = int(input("Enter a number: "))

factorial = 1
multiplier = 1

while multiplier <= number:
    factorial = factorial * multiplier
    multiplier = multiplier + 1

print("Factorial:", factorial)
