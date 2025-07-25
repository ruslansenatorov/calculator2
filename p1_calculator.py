"""Простой консольный калькулятор для двух целых чисел и базовых арифметических
операций."""


def calculator() -> None:
    """Ввод двух чисел и операции, вывод результата или ошибки."""
    no_1 = int(input("enter your first number"))
    operation = str(input("enter  arithmetic operation  like +,-,*,/"))
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
            print(f"the quotient of {no_1}  / {no_2} are {no_1 / no_2}")
    else:
        print("invalid output")


calculator()
