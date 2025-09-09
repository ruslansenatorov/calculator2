# Учебный проект "Калькулятор"

# 🧮 Calculator2

Простой калькулятор на Python, реализующий базовые арифметические операции:  
**сложение (+)**, **вычитание (-)**, **умножение (*)** и **деление (/)**.  
Запрашивает ввод у пользователя и выводит результат вычислений.  
Обрабатывает деление на ноль и некорректный ввод операций.

---

## 🔧 Установка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/ruslanenatorov/calculator2.git
cd calculator2

# установите зависимости

pip install -r requirements.txt
pre-commit install

#структура
calculator2/
├── p1_calculator.py           # Основной файл калькулятора
├── .gitignore                 # Игнорируемые файлы
├── .pre-commit-config.yaml    # Конфигурация pre-commit
├── requirements.txt           # Зависимости проекта
└── README.md                  # Этот файл

