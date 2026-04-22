total_sales = 0

while True:
    sales_amount = float(input("Enter sales (or -1 to stop): "))

    if sales_amount == -1:
        break

    total_sales += sales_amount

print("Total sales:", total_sales)
