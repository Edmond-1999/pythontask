import random

secret_number = random.randint(1, 1000)

guess = 0

print("I have chosen a number between 1 and 1000")

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low. Try again.")

    if guess > secret_number:
        print("Too high. Try again.")

    if guess == secret_number:
        print("Congratulations! You guessed the number!")
