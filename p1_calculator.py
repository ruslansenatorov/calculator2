"""Consolas calculator that performs a single arithmetic operation on two
numbers."""


def calculator() -> None:
    """Prompt the user for two numbers and an operator, then print the result.

    Supports addition, subtraction, multiplication and division. Division by zero is handled separately instead of
    raising an exception.
    """

    no_1 = int(input("enter your first number"))
    operation = input("enter arithmetic operation  like +,-,*,/")
    no_2 = int(input("enter your second number"))

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
