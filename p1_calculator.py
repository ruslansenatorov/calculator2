"""This is a simple calculator that can calculate the sum, difference, product
and division of two numbers it takes two numbers and an operation as input and
prints the result of the operation it also checks if the operation is valid and
if the second number is not zero for division it also checks if the operation
is valid and if the second number is not zero for division."""


def calculator() -> None:
    """
    this function is used to calculate the sum, difference, product and division of two numbers
    input:
        no_1: int
        operation: str
        no_2: int
    output:
        print the result of the operation
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
