user_input = input("Enter a five-digit number: ")

if user_input == user_input[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
