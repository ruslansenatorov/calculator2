"""Модуль для выполнения простых арифметических операций."""


def calculator() -> None:
    """Функция запрашивает ввод данных у пользователя и выводит результат
    операции."""
    try:
        no_1 = int(input("enter your first number: "))
        operation = input("enter arithmetic operation like +,-,*,/: ")
        no_2 = int(input("enter your second number: "))

        if operation == "+":
            print(f"the sum of {no_1} + {no_2} is {no_1 + no_2}")
        elif operation == "-":
            print(f"the diff of {no_1} - {no_2} is {no_1 - no_2}")
        elif operation == "*":
            print(f"the product of {no_1} * {no_2} is {no_1 * no_2}")
        elif operation == "/":
            if no_2 == 0:
                print("it gives infinity as it is not divided by zero")
            else:
                print(f"the quotient of {no_1} / {no_2} is {no_1 / no_2}")
        else:
            print("invalid operation")
    except ValueError:
        print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    calculator()
