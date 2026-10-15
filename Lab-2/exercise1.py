"""Lab 2 - Exercise 1: if / elif / else.

Task: read a whole number and say whether it is positive, negative or zero,
and whether it is even or odd.

Example:
    Enter a whole number: -7
    -7 is negative and odd.

Run:  uv run python Lab-2/exercise1.py
"""

number = int(input("Enter a whole number: "))

if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

parity = "even" if number % 2 == 0 else "odd"

print(f"{number} is {sign} and {parity}.")
