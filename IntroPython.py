"""

Xx1=int (input("Я жду число1:"))
xX2=int (input ("И ещё число2:"))
print (Xx1+xX2)
first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum = ", str(sum))
third = float(input("Third: "))
print(third % 3)


Форматирование вьівода

# простое форматирование:
x = 5; y = 10; z = 25 
print('Значение х = {}, а y = {}, но z = {}'.format(x,y,z))

# использование кортежа:
print('Я люблю {0} и {1}'.format('хлеб', 'масло'))
print('Я люблю {1} и {0}'.format('хлеб', 'масло'))

# Для форматирования строк можно использовать именованные аргументы. Вывод: Привет, Иван, доброго утра
print('Привет, {имя}, {пожелания}'.format(пожелания = 'доброго утра', имя = 'Иван'))


Строки документации (docstrings) в Python
Docstring — это сокращение от documentation string (строка документации).

Строки документации в Python — это строковые литералы, которые появляются сразу после определения функции, метода, класса или модуля.

При написании строк документации используются тройные кавычки. Например:
"""


def double(num): 
    return 2*num
print(double.__doc__)
print(double("summer"))


a, b = int(input()), int(input())
print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5, sep='\n')

