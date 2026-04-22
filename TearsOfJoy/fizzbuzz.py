for number in range(1, 51):
    print(number)

    if number % 3 == 0:
        print("Fizz")

    if number % 5 == 0:
        print("Buzz")

    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")
