'''
collect input for the price
if price is greater than or equal to 1000 and less than or equal to 10000, discounted price would be 95 percent
if price is greater than 10000 and less than or equal to 50000, discounted price would be 90 percent
if price is greater than 50000, discounted price would be 80 percent
calculate the discounted price by multiplying by price
print the discounted price
'''
price = int(input("Enter the price of the item: "))

if price >= 1000 and price <= 10000:
    print("Your discount is 5%")
    discount = 95/100

elif price > 10000 and price <= 50000:
    print("Your discount is 10%")
    discount = 90/100

elif price > 50000:
    print("Your discount is 20%")
    discount = 80/100

discounted_price = price * discount

print("Your discounted price is", discounted_price)
