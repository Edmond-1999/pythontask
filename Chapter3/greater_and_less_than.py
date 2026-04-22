"""
If your row is odd, print the greater than symbol
Else print the less than symbol
"""

for row in range(10):
    for column in range(10):
        print("<" if row % 2 == 1 else ">", end = " ")
    print()
