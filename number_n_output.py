"""
Алгоритм получения цифр n--значного числа

1-й способ:
Последняя цифра(единица): (num % 10) // 1;
Предпоследняя цифра(десятки): (num % 100) // 10;
Предпредпоследняя цифра(): (num % 10000) // 100;
.....
Вторая цифра: (num % 10**n-1) // 10**n-2;
Первая цифра: (num % 10**n) // 10**n-1.

2-й способ
123456789  // 1 % 10 ---> 9                (единицы)
123456789   // 10 % 10 ---> 8               (десятки)
123456789  // 100 % 10 ---> 7               (сотни)
123456789  // 1000 % 10 ---> 6             (тысячи)
123456789  // 10000 % 10 ---> 5           (десятки тысяч)
123456789  // 100000 % 10 ---> 4         (сотни тысяч)
123456789  // 1000000 % 10 ---> 3       (миллионы)
123456789  // 10000000 % 10 ---> 2     (десятки миллионов)
123456789  // 100000000 % 10 ---> 1   (сотни миллионов)
"""

num = int(input())
first_digit = num % 10
second_digit = num % 100 // 10
third_digit = num % 1000 // 100
forth_digit = num % 10000// 1000
print('forth_digit % 10000 =', forth_digit)
a = str(first_digit)
b = str(second_digit)
c = str(third_digit)
d = str(forth_digit)
print('Цифра в позиции тысяч равна', d)  # 
print('Цифра в позиции сотен равна', c)
print('Цифра в позиции десятков равна', b)
print('Цифра в позиции единиц равна', a)