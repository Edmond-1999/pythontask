"""
collect input for password
get the length of the password
if the password length is less thsn 8, print "Very Weak"
or if the password length is equal to 8 print "Weak"
if the password length is greater than 8 and less than or equal to 16, print "Strong"
if the password length is greater than 16, print "Very Strong"
"""
password = input("Enter a password: ")
password_length = len(password)

if password_length < 8:
    print("Very Weak")

elif password_length == 8:
    print("Weak")

elif password_length > 8 and password_length <= 16:
    print("Strong")

elif password_length > 16:
    print("Very Strong")
