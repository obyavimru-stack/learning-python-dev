# задание 1 - сравнение двух чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
     print("Первое число больше второго")
elif b > a:
     print("Второе число больше первого")
else:
     print("Первое равно второму")

# задание 2 - число или нет
try:
    znak =int(input("Введите число: "))
    print("Это число")
except ValueError:
    print("Ошибка: введите число")
    
# задание 3 - площадь квадрата
st = int(input("Введите сторону квадрата: "))
pl = st*st
print("Площадь квадрата:",pl)

# задание 4 - конвертер времени
sec = int(input("Введите количество секунд: "))
min = sec/60
print("Это",min,"минут")

chas = sec/3600
print("Это",chas,"часов")

# задание 5 - проверка температуры
temp = int(input("Введите температуру: "))
if temp >= 30:
    print("Жарко")
elif 15 <= temp < 30:
    print("Тепло")
elif 0 <= temp <= 14:
    print("Прохладно")
else:
    print("Холодно")

# задание 6 - деление с проверкой
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if b == 0:
    print("На ноль делить нельзя")
else:
    print(a/b)

# задание 7 -простой кредитный рейтинг
doh = int(input("Введите сумму дохода: "))
if doh == 100000:
    print("Высокий доход")
elif 50000 <= doh <= 99999:
    print("Средний доход")
elif doh < 50000:
    print("Низкий доход")

# задание 8 - четверть часа
ch = int(input("Введите число от 0 до 59: "))
if 0 <= ch <=14:
     print("1-я четверть")
elif 15 <= ch <= 29:
     print("2-я четверть")
elif 30 <= ch <= 44:
    print("3-я четверть") 
elif 45 <= ch <= 59:
    print("4-я четверть")
else:
    print("Ошибка")

#  задание 9 - цена товара с НДС
cen = int(input("Введите цену: "))
nds = cen + cen*0.2
print("Цена товара с НДС:",nds)

# задание 10 - сравнение трёх чисел
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
elif value_b < value_a and value_b < value_c
    print("Самое маленькое число:", value_b)
else:
    print("Самое маленькое число:", value_c)

if value_a == value_b or value_a == value_c or value_b == value_c:
    print("Есть одинаковые числа")
else:
    print("Все числа разные")


с = a/b

