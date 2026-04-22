correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts = attempts + 1

        if attempts == 3:
            print("Locked out")
