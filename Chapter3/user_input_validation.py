passes = 0
failures = 0
counter = 0

sentinel = 1

while sentinel > 0:
    result = int(input("Enter result (1=pass, 2=fail): "))

    if result == 1:
        counter = counter + 1
        passes = passes + 1

    elif result == 2:
        counter = counter + 1
        failures = failures + 1
    else:
        print("invalid score")

    if counter == 10:
        break


print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')


