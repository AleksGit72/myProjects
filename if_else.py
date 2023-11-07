"""
  Выражение  	Описание
if x > 7	если x больше 7
if x < 7	если x меньше 7
if x >= 7	если x больше либо равен  7
if x <= 7	если x меньше либо равен  7
if x == 7	если x равен  7
if x != 7	если x не равен  7
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