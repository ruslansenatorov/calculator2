"""Console calculator for basic arithmetic operations."""


def read_number(prompt: str) -> int:
    """Read an integer number from the console."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def calculator() -> None:
    """Простой консольный калькулятор.

    - запрашивает два целых числа и арифметическу операцию
    - выполняет операции '+','-','*','/'
    - выводит результат или сообщение об ошибке.
    """
    no_1 = read_number("Enter your first number: ")
    operation = input("Enter an arithmetic operation (+, -, *, /): ").strip()
    no_2 = read_number("Enter your second number: ")

    if operation == "+":
        print(f"The sum of {no_1} + {no_2} is {no_1 + no_2}.")
    elif operation == "-":
        print(f"The difference of {no_1} - {no_2} is {no_1 - no_2}.")
    elif operation == "*":
        print(f"The product of {no_1} * {no_2} is {no_1 * no_2}.")
    elif operation == "/":
        if no_2 == 0:
            print("Division by zero is not allowed.")
        else:
            print(f"The quotient of {no_1} / {no_2} is {no_1 / no_2}.")
    else:
        print("Invalid operation.")


if __name__ == "__main__":
    calculator()
