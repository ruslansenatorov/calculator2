"""Module "p1_calculator".

this module allows you to perform basic arithmetical operations
with two required integer numbers.

function:
    calculator: perform basic arithmetic operations like addition, subtraction, multiplication and division.
"""


def calculator() -> None:
    """It's a simple calculator which can perform basic arithmetic operations
    like addition, subtraction, multiplication and division."""
    no_1 = int(input("enter your first number"))
    operation = input("enter  arithmetic operation  like +,-,*,/")
    no_2 = int(input("enter your  second number"))

    if operation == "+":
        print(f"the sum of {no_1} + {no_2} are {no_1 + no_2}")
    elif operation == "-":
        print(f"the diff of {no_1}  - {no_2} are {no_1 - no_2}")
    elif operation == "*":
        print(f"the product of {no_1} * {no_2} are {no_1 * no_2}")
    elif operation == "/":
        if no_2 == 0:
            print("it gives infinity as it is not divided by zero")
        else:
            print(f"the sum of {no_1}  / {no_2} are {no_1 / no_2}")
    else:
        print("invalid output")


calculator()
