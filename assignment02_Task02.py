"""
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""
print("")

null = 0

for i in range(1, 51):
    print(i)
    null += i

print(f"The sum of all integers from 1 to 50 is {null}.")
