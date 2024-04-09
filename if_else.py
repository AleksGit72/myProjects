"""
  Выражение  	Описание
if x > 7	если x больше 7
if x < 7	если x меньше 7
if x >= 7	если x больше либо равен  7
if x <= 7	если x меньше либо равен  7
if x == 7	если x равен  7
if x != 7	если x не равен  7
"""
"""
num1 = int(input('num1 = '))
num2 = int(input('num2 = '))
if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)
if num1 == num2:                      # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)

# программа, которая считывает три числа и подсчитывает количество чётных чисел.
num1, num2, num3 = int(input('Введите число1: ')), int(input('Введите число2: ')), int(input('Введите число3: '))
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print('Введено', counter, 'чётных чисел')


#  1-й вариант Наименьшее из четырёх чисел(13 строк):
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
if num1 <= num2:
    min1 = num1
else:
    min1 = num2
if num3 <= num4:
    min2 = num3
else:
    min2 = num4
if min1 <= min2:
    print(min1)
else:
    print(min2)

#  2-й вариант Наименьшее из четырёх чисел(9 строк!!!):
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
if num1 >= num2:
    num1 = num2
if num1 >= num3:
    num1 = num3
if num1 >= num4:
    print(num4)
else:
    print(num1)

#  Программа, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
age = int(input())
if 0 < age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if 60 <= age <= 150:
    print('старость')
"""

num1, num2, num3 = int(input()), int(input()), int(input())
s = 0
if num1 > 0:
    s = s + num1
if num2 > 0:
    s = s + num2
if num3 > 0:
    s = s + num3
print(s)
