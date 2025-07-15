"""p1_calculator.py module
A simple console calculator module implementing basic arithmetic operations:
addition, subtraction, multiplication, and division. Prompts for user input and outputs the calculation result.
Handles division by zero and invalid operation input.

Functions:
— calculator(): launches an interactive calculator in the console.
"""


def calculator() -> None:
    """
    A simple console calculator:
    — Prompts for two integers and an arithmetic operation;
    — Performs the arithmetic operation: +, -, *, /;
    — Outputs the result or an error message.
    """
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
