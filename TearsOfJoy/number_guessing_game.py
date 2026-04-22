import random

number = random.randint(0, 100)
guess = 0
counter = 0


while guess != number:
    guess = int(input("Enter your guess (1–100): "))

    if guess < number:
        counter = counter + 1
        print("Higher")
    elif guess > number:
        counter = counter + 1
        print("Lower")
    else:
        counter = counter + 1
        print("Correct!", number)


print(counter, " attempts")
