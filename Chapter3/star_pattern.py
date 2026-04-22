row_count = int(input("Enter number of rows: "))

for row in range(1, row_count + 1):
    for column in range(row):
        print("*", end="")
    print()
