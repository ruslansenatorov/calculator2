"""Модуль calculator.py.

Простой консольный калькулятор, реализующий базовые арифметические операции:
сложение, вычитание, умножение и деление. Запрашивает ввод от пользователя
и выводит результат вычислений. Обрабатывает деление на ноль и некорректный ввод операции.

Функции:
 - calculator(): запускает интерактивный калькулятор в консоли.
"""


def calculator() -> None:
    """Простой консольный калькулятор:

    - Запрашивает два целых числа и арифметические операции
    - Выполняет операцию: +, -, *, /
    - Выводит результат или сообщение об ошибке
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
