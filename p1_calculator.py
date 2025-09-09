"""Модуль calculator.py.

Простой консольный калькулятор, реализующий базовые арифметические операции: сложение,
вычитание, умножение и деление. Запрашивает ввод от пользователя и выводит результат
вычислений. Обрабатывает деление на ноль и некорректный ввод операции.

Функции:     calculator(): запускает интерактивный калькулятор в консоли.
"""


def calculator() -> None:
    """Запускает интерактивный калькулятор в консоли."""
    try:
        no_1 = int(input("Enter your first number: "))
        operation = input("Enter arithmetic operation (+, -, *, /): ").strip()
        no_2 = int(input("Enter your second number: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    result: float  # Аннотация — mypy теперь знает, что result может быть float
    if operation == "+":
        result = no_1 + no_2
        print(f"The sum of {no_1} + {no_2} is {result}")
    elif operation == "-":
        result = no_1 - no_2
        print(f"The difference of {no_1} - {no_2} is {result}")
    elif operation == "*":
        result = no_1 * no_2
        print(f"The product of {no_1} * {no_2} is {result}")
    elif operation == "/":
        if no_2 == 0:
            print("Cannot divide by zero!")
        else:
            result = no_1 / no_2
            print(f"The division of {no_1} / {no_2} is {result}")
    else:
        print("Invalid operation. Please use +, -, *, or /.")


if __name__ == "__main__":
    calculator()
