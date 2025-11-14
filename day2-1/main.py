# задание 1
try:
    login = int(input("Введите логин: "))
    pwd = int(input("Введите пароль: "))
    if login == "admin" and pwd == "12345"
        print("Вход выполнен")
except ValueError:
        print("Неверный логин или пароль")

# задание 2
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    op = input("Введите операцию: (+),(-),(*),(/): ")
    if op == "+":
        c = a + b
        print(c)
    elif op == "-":
        c = a - b
        print(c)
    elif op == "*":
        c = a * b
        print(c)
    elif op == "/":
        c = a / b
        print(c)
except ValueError:
        print("Введено не числовое значение")

# задание 3
try:
    mes = int(input("Введите номер месяца: "))
    if 12 == mes < 3:
        print("Декабрь,Январь,Февраль -> Зима")
    elif 3 <= mes < 5:
        print("Март,Апрель,Май -> Весна")
    elif 5 < mes < 9:
        print("Июнь,Июль,Август -> Лето")
    elif 9 <= mes < 12:
        print("Сентябрь,Октябрь,Ноябрь -> Осень")
except ValueError:
        print("Введите число от 1 до 12")

# задание 4
try:
    value_a = int(input("Введите первое число: "))
    value_b = int(input("Введите второе число: "))
    value_c = int(input("Введите третье число: "))
    if value_a > value_b and value_a > value_c:
        print("Самое большое число:", value_a)
    elif value_b > value_a and value_b > value_c:
        print("Самое большое число:", value_b)
    elif value_c > value_a and value_c > value_b:
        print("Самое большое число:", value_c)

    if value_a < value_b and value_a < value_c:
        print("Самое маленькое число:",value_a)
    elif value_b < value_a and value_b < value_c:
        print("Самое маленькое число:", value_b)
    elif value_c < value_a and value_c < value_b:
        print("Самое маленькое число:",value_c)
except ValueError:
    print("Ошибка ввода")

# задание 5
try:
except ValueError:

# задание 6
try:
except ValueError:

# задание 7
try:
except ValueError:

# задание 8
try:
except ValueError:

# задание 9
try:
except ValueError:

# задание 10
try:
except ValueError:
