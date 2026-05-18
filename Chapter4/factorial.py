number = int(input("Enter a number: "))

factorial = 1

for counter in range(1, number + 1):
    factorial *= counter

print("Factorial:", factorial)
