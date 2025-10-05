"""
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""

print("")

num = int(input("Please enter the number: "))

remainder = num % 2

if remainder == 0:
    print("The given number is even.")
else:
    print("The given number is odd.")
