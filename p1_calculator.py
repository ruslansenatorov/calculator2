"""This module provides a simple command-line calculator.

It contains one main function `calculator()` which allows the user to perform basic arithmetic operations (+, -, *, /)
on two integer inputs.
"""


def calculator() -> None:
    """Runs a simple interactive calculator.

    Prompts the user to input two numbers and an arithmetic operation. It then performs the calculation and prints the
    result. Handles division by zero error by printing an appropriate message. If an invalid operator is entered, it
    prints 'invalid output'.
    """
    no_1 = int(input("enter your first number: "))
    operation = input("enter arithmetic operation like +,-,*,/: ")
    no_2 = int(input("enter your second number: "))

    if operation == "+":
        print(f"the sum of {no_1} + {no_2} is {no_1 + no_2}")
    elif operation == "-":
        print(f"the difference of {no_1} - {no_2} is {no_1 - no_2}")
    elif operation == "*":
        print(f"the product of {no_1} * {no_2} is {no_1 * no_2}")
    elif operation == "/":
        if no_2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"the result of {no_1} / {no_2} is {no_1 / no_2}")
    else:
        print("invalid output")


# run calculator
calculator()
