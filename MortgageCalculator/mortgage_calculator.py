principal = int(input("Enter principal amount: "))
annual_rate = int(input("Enter the annual rate interest: "))
time = int(input("Enter the duration in years: "))

rate = (annual_rate / 100) / 12

months_duration = time * 12

monthly_payment = principal * (rate * ((1 + rate) ** months_duration)) / ((1 + rate) ** months_duration - 1)

print("Your monthly payment is:$", round(monthly_payment, 2))
