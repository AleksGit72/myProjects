"""
Алгоритм получения цифр n--значного числа

Последняя цифра(единица): (num % 10) // 1;
Предпоследняя цифра(десятки): (num % 100) // 10;
Предпредпоследняя цифра(): (num % 10000) // 100;
.....
Вторая цифра: (num % 10**n-1) // 10**n-2;
Первая цифра: (num % 10**n) // 10**n-1.
"""

num = int(input())
first_digit = num % 10
second_digit = num % 100 // 10
third_digit = num % 1000 // 100
forth_digit = num % 10000// 1000
a = str(first_digit)
b = str(second_digit)
c = str(third_digit)
d = str(forth_digit)
print('Цифра в позиции тысяч равна', str(d))
print('Цифра в позиции сотен равна', str(c))
print('Цифра в позиции десятков равна', str(b))
print('Цифра в позиции единиц равна', str(a))