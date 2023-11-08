""""
and — логическое умножение;
or — логическое сложение;
not — логическое отрицание.

Приоритеты логических операторов
Логические операторы, подобно арифметическим операторам (+, -, *, /), имеют приоритет выполнения. Приоритет выполнения следующий:

в первую очередь выполняется логическое отрицание not;
далее выполняется логическое умножение and;
далее выполняется логическое сложение or.
"""
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if -1 <= x2 - x1 <= 1 and -1 <= y2 - y1 <= 1:
    print('YES')
else:
    print('NO')