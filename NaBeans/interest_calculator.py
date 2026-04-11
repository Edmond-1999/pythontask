principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate (%): "))
time = float(input("Enter the time (years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("Simple Interest is:", simple_interest)
print("Total Amount is:", total_amount)
