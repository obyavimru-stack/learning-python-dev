# задание 1
login = input("Введите логин: ")
pwd = input("Введите пароль: ")

if login == "admin" and pwd == "12345":
    print("Вход выполнен")
else:
    print("Неверный логин или пароль")


# задание 2
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    op = input("Введите операцию: (+),(-),(*),(/): ")

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("Делить на ноль нельзя")
        else:
            print(a / b)
    else:
        print("Неизвестная операция")

except ValueError:
    print("Введено не числовое значение")


# задание 3
try:
    mes = int(input("Введите номер месяца: "))
    if mes == 12 or mes == 1 or mes == 2:
        print("Зима")
    elif 3 <= mes <= 5:
        print("Весна")
    elif 6 <= mes <= 8:
        print("Лето")
    elif 9 <= mes <= 11:
        print("Осень")
    else:
        print("Введите число от 1 до 12")

except ValueError:
    print("Введите число")


# задание 4
try:
    value_a = int(input("Введите первое число: "))
    value_b = int(input("Введите второе число: "))
    value_c = int(input("Введите третье число: "))

    if value_a > value_b and value_a > value_c:
        print("Самое большое число:", value_a)
    elif value_b > value_a and value_b > value_c:
        print("Самое большое число:", value_b)
    else:
        print("Самое большое число:", value_c)

    if value_a < value_b and value_a < value_c:
        print("Самое маленькое число:", value_a)
    elif value_b < value_a and value_b < value_c:
        print("Самое маленькое число:", value_b)
    else:
        print("Самое маленькое число:", value_c)

    if value_a == value_b or value_a == value_c or value_b == value_c:
        print("Есть одинаковые числа")
    else:
        print("Все числа разные")

except ValueError:
    print("Ошибка ввода")


# задание 5
try:
    year = int(input("Введите год: "))

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный год")

except ValueError:
    print("Введите год")


# задание 6
try:
    age = int(input("Введите возраст: "))

    if age < 0:
        print("Ошибка: возраст не может быть отрицательным")
    elif age <= 6:
        print("Маленький ребёнок")
    elif age <= 12:
        print("Ребёнок")
    elif age <= 17:
        print("Подросток")
    elif age <= 30:
        print("Молодой взрослый")
    elif age <= 60:
        print("Взрослый")
    else:
        print("Пожилой")

except ValueError:
    print("Введите число")


# задание 7
try:
    hours = int(input("Введите количество часов: "))

    if hours < 0:
        print("Ошибка: количество часов не может быть отрицательным")
    else:
        print("Минут:", hours * 60)
        print("Секунд:", hours * 3600)

except ValueError:
    print("Введите число")


# задание 8
try:
    score = int(input("Введите балл (0-100): "))

    if 90 <= score <= 100:
        print("Отличная кредитоспособность")
    elif 70 <= score <= 89:
        print("Хорошая")
    elif 50 <= score <= 69:
        print("Средняя")
    elif 30 <= score <= 49:
        print("Низкая")
    elif 0 <= score <= 29:
        print("Очень низкая")
    else:
        print("Ошибка: балл вне диапазона 0-100")

except ValueError:
    print("Введите число")


# задание 9
try:
    wl = int(input("Введите длину волны (нм): "))

    if 380 <= wl <= 450:
        print("Фиолетовый")
    elif 451 <= wl <= 495:
        print("Синий")
    elif 496 <= wl <= 570:
        print("Зелёный")
    elif 571 <= wl <= 590:
        print("Жёлтый")
    elif 591 <= wl <= 620:
        print("Оранжевый")
    elif 621 <= wl <= 750:
        print("Красный")
    else:
        print("Не входит в видимый спектр")

except ValueError:
    print("Введите число")


# задание 10
try:
    age = int(input("Введите возраст: "))
    student = input("Есть студенческий билет? (yes/no): ")

    if age < 0:
        print("Ошибка возраста")
    elif age < 12:
        price = 100
    elif age <= 17:
        price = 150
    elif age <= 59:
        price = 300
    else:
        price = 120

    if 18 <= age <= 25 and student == "yes":
        price = price / 2

    print("Цена билета:", price)

except ValueError:
    print("Введите возраст числом")
