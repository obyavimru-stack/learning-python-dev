# -----------------------------
# 1. Чётное / нечётное
# -----------------------------
try:
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print("Чётное")
    else:
        print("Нечётное")
except ValueError:
    print("Ошибка: введено не число!")


# -----------------------------
# 2. Положительное / отрицательное / ноль
# -----------------------------
try:
    number = int(input("Введите число: "))
    if number > 0:
        print("Положительное")
    elif number < 0:
        print("Отрицательное")
    else:
        print("Ноль")
except ValueError:
    print("Ошибка: введите целое число")


# -----------------------------
# 3. Сравнение двух чисел
# -----------------------------
try:
    a_value = int(input("Введите число (a): "))
    b_value = int(input("Введите число (b): "))

    if a_value > b_value:
        print("a больше b")
    elif a_value < b_value:
        print("a меньше b")
    else:
        print("a равно b")
except ValueError:
    print("Ошибка: необходимо вводить только числа")


# -----------------------------
# 4. Проверка доступа по возрасту
# -----------------------------
try:
    age = int(input("Введите ваш возраст: "))
    if age >= 18:
        print("Доступ разрешён")
    elif 0 <= age < 18:
        print("Доступ запрещён")
    else:
        print("Возраст не может быть отрицательным")
except ValueError:
    print("Ошибка: возраст должен быть числом")


# -----------------------------
# 5. Мини-виджет оценки (0–100)
# -----------------------------
try:
    score = int(input("Введите SCORE (0–100): "))

    if not 0 <= score <= 100:
        print("Ошибка: балл должен быть от 0 до 100")

    elif score >= 90:
        print("A")
    elif score >= 75:
        print("B")
    elif score >= 60:
        print("C")
    elif score >= 40:
        print("D")
    else:
        print("F")

except ValueError:
    print("Ошибка: необходимо ввести число")

