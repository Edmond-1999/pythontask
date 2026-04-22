hours_parked = float(input("Enter hours parked: "))

if hours_parked <= 3:
    charge = 2.00
else:
    extra_time = hours_parked - 3
    charge = 2.00 + (extra_time * 0.50)

if charge > 10:
    charge = 10.00

print("Parking charge: $", charge)
