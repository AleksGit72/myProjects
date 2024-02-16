'''
# Функция — это группа связанных инструкций, выполняющих определенную задачу.

# Функции помогают разбить нашу программу на более мелкие части. 
# По мере того, как наша программа становится все больше и больше, функции делают ее более организованной и управляемой.

# Кроме того, функцию можно вызвать из различных мест программы, что позволяет избежать повторения программного кода.


#Синтаксис функции:
#def имя_функции(аргументы):
#   """строка документации"""
#   операторы
def triple(x):
    """Функция, которая утраивает значение вводимого аргумента"""
    return int(x)*3

a = input("Input number a = ")
print(triple.__doc__) # печатает сроку документации(описание) функции
print("3*a = ", triple(a))

def cube(x):
    """Функция, которая значение вводимого аргумента возводит в 3-ю степень"""
    return float(x)**3

a = input("Input number a = ")
print(cube.__doc__) # печатает сроку документации(описание) функции
print("a^3 = ", cube(a))

def absolute_value(num):
    """ Возвращает абсолютное значение введенного числа"""

    if num >= 0:
        return num
    else:
        return -num
print(absolute_value.__doc__)
a = input("nunber1 = ")
b = input("number2 =  ") 
print(absolute_value(float(a)))
print(absolute_value(float(b)))

# На вход программе подается два числа y и x, каждое на отдельной строке.
# Программа  выводит "пустой"(незаполненный внутри) звездный прямоугольник с размерами у(строк) на х(столбцов)
def draw_box(y, x):
     for i in range(y):
          print('*' * x if i == 0 or i == y - 1 else '*' + ' ' * (x - 2) + '*')

draw_box(int(input()), int(input()))


# Напишите функцию draw_triangle(fill, base),  которая принимает два параметра:
# fill – символ заполнитель и base – основание равнобедренного треугольника(строго нечетное), каждый на отдельной строке.
# Программа  выводит  прямоугольник из заполнителя fill с основанием base. 
def draw_triangle(fill, base):
    for _ in range(1, base // 2 + 1): print(fill * _)
    for _ in range(base + 1, base // 2 + 1, -1): print( fill * (_ - base // 2 - 1))

draw_triangle(input(), int(input()))




def print_fio(name, surname, patronymic):
    """
    Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
    name – имя человека;
    surname – фамилия человека;
    patronymic – отчество человека;
    Программа  выводит на печать ФИО человека (все три буквы в ФИО должны иметь верхний регистр).
    """
    print(surname[0] + name[0] + patronymic[0])

print(print_fio.__doc__) # выводит документацию на функцию
print_fio(input().upper(), input().upper(), input().upper())



def print_digit_sum(num):
    """
    Функция print_digit_sum()
    Принимает одно целое число и выводит на печать сумму его цифр.
    """
    lst = [int(i) for i  in str(num)]
    print(sum(lst))

print(print_digit_sum.__doc__)
print_digit_sum(int(input('Введите число: ')))


'''