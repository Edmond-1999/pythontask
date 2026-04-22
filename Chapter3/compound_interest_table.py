principal_amount = 1000
interest_rate = 0.05

print("Year\tAmount")

for year in range(1, 11):
    amount = principal_amount * (1 + interest_rate) ** year
    print(year, "\t", round(amount, 2))
