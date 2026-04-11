number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

totalSum = number1 + number2 + number3
averageValue = totalSum / 3

productValue = number1 * number2 * number3

smallestValue = min(number1, number2, number3)
largestValue = max(number1, number2, number3)

print("Sum:", totalSum)
print("Average:", averageValue)
print("Product:", productValue)
print("Smallest:", smallestValue)
print("Largest:", largestValue)
