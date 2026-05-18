def fahrenheit(celsius):
    return (9 / 5) * celsius + 32


print("Celsius    Fahrenheit")

for celsius in range(0, 101):
    print(celsius, "    ", fahrenheit(celsius))
