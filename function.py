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




def convert_to_miles(km):
    """
    Функция принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях.
    """
    return km * 0.6214

print(convert_to_miles.__doc__)
print(convert_to_miles(float(input())))




def get_days(month):  # объявление функции
    """
    Функция принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.
    Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
    Гарантируется, что что год является невисокосным.
    """
    if month == 2: return 28
    elif month in [4, 6, 9, 11]: return 30
    else: return 31

print(get_days.__doc__)   
print('В месяце', get_days(int(input('Введите номер месяца невисокосного года: '))), 'дней.')  # вызываем функцию



def get_factors(num):
    """
    Функция принимает в качестве аргумента натуральное число и возвращает список всех делителей данного числа.
    """
    return [i for i in range(1, num // 2 + 1) if num % i == 0] + [num]

print(get_factors.__doc__)
print('Cписок всех делителей данного числа:', get_factors(int(input('Введите целое число: '))))



def number_of_factors(num):
    """
    Функция принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.
    """
    return len([i for i in range(1, num // 2 + 1) if num % i == 0] + [num])
    
print(number_of_factors.__doc__)
print('Количество всех делителей данного числа:', number_of_factors(int(input('Введите целое число: '))))




def find_all(target, symbol):
    """  
    Функция find_all(target, symbol) принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.
    Если указанный символ не встречается в строке, то возвращается пустой список.
    """
    return [i for i in range(len(target)) if target[i] == symbol]
print(find_all.__doc__)
print('Cписок, содержащий все местоположения  символа "symbol" в строке "target": ', find_all(input('Введите строку "target": '), input('Введите символ "symbol": ')))




def merge(list1, list2):
    """
    Функция принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.
    """
    list1.extend(list2)
    list1.sort()
    return list1
print(merge.__doc__)
print('Объединненный отсортированный список: ', merge([int(c) for c in input('Введите список 1: ').split()], [int(c) for c in input('Введите список2: ').split()]))




def quick_merge(list1, list2):
    """
    Merge lists 2
    На вход программе подается натуральное число n, а затем n строк, содержащих целые числа в порядке возрастания, разделенные символом пробела.
    Программа объединяет указанные списки в один отсортированный список с помощью функции quick_merge() и выводит элементы окончательного списка каждое через пробел.
    Функция быстрого слияния quick_merge() : https://stepik.org/lesson/331754/step/12?unit=315133
    """
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2
    while p1 < len(list1) and p2 < len(list2):  # пока не закончились оба списка
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    return result

total_list = []
for i in range(int(input('Введите количество списков для сортировки: '))):
    num = [int(j) for j in input('Введите список для сортировки: ').split()]
    total_list = quick_merge(total_list, num)

print(quick_merge.__doc__)
print('Объединненный отсортированный список: ', *total_list)



def is_valid_triangle(a, b, c):
    """
    Функция: Is Valid Triangle?
    На вход функции подается три натуральных числа, после возвращается True если существует невырожденный треугольник со сторонами а, b, с и False в противном случае.
    """
    return (a + b) > c and (a + c) > b and (b + c) > a

print(is_valid_triangle.__doc__, 'Введите стороны треугольника:', sep='\n')  
print('Данный треугольник невырожденный: ', is_valid_triangle(int(input('side1 = ')), int(input('side2 = ')), int(input('side3 = '))))





def is_prime(num):
    """
    Функция: Is a Number Prime?
    На вход функции подается в качестве аргумента натуральное число и возвращается значение True если число является простым и False в противном случае.
    """
    counter = 0
    for i in range(1, num // 2 + 1):
        if counter >= 2:
            break        
        if num % i == 0:
            counter += 1
    counter += 1
    return counter == 2 
        
print(is_prime.__doc__)
print('Число является простым? ', is_prime(int(input('Введите целое число: '))))




def is_prime(num):
    """
    Функция: Is a Number Prime?
    На вход функции подается в качестве аргумента натуральное число и возвращается значение True если число является простым  и False в противном случае.
    """
    return len([_ for _ in range(1, num // 2 + 1) if num % _ == 0]) + 1 == 2
        
print(is_prime.__doc__)
print('Число является простым? ', is_prime(int(input('Введите целое число: '))))




def is_prime(num):
    """
    Функция: is_prime(num)
    На вход функции подается в качестве аргумента натуральное число и возвращается значение True если число является простым  и False в противном случае.
    """
    return len([_ for _ in range(1, num // 2 + 1) if num % _ == 0]) + 1 == 2
def get_next_prime(num):
    """
    Функция: get_next_prime(num)
    На вход функции подается в качестве аргумента натуральное число и возвращается первое простое число большее числа num.
    """

    num += 1
    while True:
        if is_prime(num):
            return num
        else:
            num += 1
print(get_next_prime.__doc__)
print('Первое простое число большее введенного числа: ', get_next_prime(int(input('Введите целое число: '))))



def is_prime(num):
    """
    Функция: is_prime(num)
    На вход функции подается в качестве аргумента натуральное число и возвращается значение True если число является простым  и False в противном случае.
    """
    return len([_ for _ in range(1, num // 2 + 1) if num % _ == 0]) + 1 == 2
def get_next_prime(num):
    """
    Функция: get_next_prime(num)
    На вход функции подается в качестве аргумента натуральное число и возвращается первое простое число большее числа num.
    """

    num += 1
    while not is_prime(num):
        num += 1
    return num

print(get_next_prime.__doc__)
print('Первое простое число большее введенного числа:', get_next_prime(int(input('Введите целое число: '))))







def is_password_good(password):
    """
    Функция: is_password_good(password)
    На вход функции подается в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является надежным и False - в противном случае.
    Пароль является надежным если:
        его длина не менее 8 символов;
        он содержит как минимум одну заглавную букву (верхний регистр);
        он содержит как минимум одну строчную букву (нижний регистр);
        он содержит хотя бы одну цифру.
    """

    return  len(password) >= 8 and not password.isalpha() and not password.isdigit() and not password.isupper() and not password.islower()  and password.isalnum() 

print(is_password_good.__doc__)
print('Пароль надежен:', is_password_good(input('Введите "password" на проверку:')))



def is_one_away(word1, word2):
    """
    Функция: one_away(word1, word2)
    На вход функции подается в качестве аргументов два слова word1 и word2 
    и возвращается значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе и False в противном случае.
    """
    count = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
    return count == 1

print(is_one_away.__doc__)   
print('Cлова имеют одинаковую длину и отличаются ровно в одном символе:', is_one_away(input('Введите word1 на проверку:'), input('Введите word2 на проверку:')))



def is_one_away(word1, word2):
    """
    Функция: one_away(word1, word2)
    На вход функции подается в качестве аргументов два слова word1 и word2 
    и возвращается значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе и False в противном случае.
    """
    if len(word1) != len(word2):
        return False
    else:
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
    if count == 1: return True
    else: return False

print(is_one_away.__doc__)   
print('Cлова имеют одинаковую длину и отличаются ровно в одном символе:', is_one_away(input('Введите word1 на проверку: '), input('Введите word2 на проверку: ')))





def is_palindrome(text):
    """
    Функция: is_palindrome(text)
    На вход функции подается в качестве аргумента строкf text и возвращается значение True если указанный текст является палиндромом и False в противном случае.
    Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
    Примечание 2. При проверке считается что большие и маленькие буквы одинаковые, а также игнорируются пробелы и символы , . ! ? -.

    """
    text = "".join(i.lower() for i in text if i.isalpha())
    return text == text[::-1]

print(is_palindrome.__doc__)
print('Текст является палиндромом:', is_palindrome(input('Введите text на проверку: ')))




def is_valid_password(password):
    """
    Функция is_valid_password(password) принимает в качестве аргумента строковое значение пароля password и возвращает значение True,
    если пароль является действительным паролем BEEGEEK банка и False - в противном случае.

    Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.  

    """
    return len(password) == 3 and is_palindrome(password[0]) and is_prime(int(password[1])) and int(password[2]) % 2 == 0

def is_palindrome(text):  # вспомогательная функция (проверка на палиндром)
    text = "".join(i.lower() for i in text if i.isdigit())
    return text == text[::-1]

def is_prime(num):  # вспомогательная функция (проверка на простое число)
    return len([_ for _ in range(1, num // 2 + 1) if num % _ == 0]) + 1 == 2

print(is_valid_password(input().split(':')))



def is_correct_bracket(text):
    """
    Функция is_correct_bracket(text) принимает в качестве аргумента непустую строку text, состоящую из символов '(' и ')'
    и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.
    
    Ведите скобочную последовательность на проверку:
    """
    while '()' in text:
        text = text.replace('()', '')
    return not text

print(is_correct_bracket.__doc__)
print('Result:', is_correct_bracket(input()))



def convert_to_python_case(text):
    """
     convert_to_python_case(text) принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
    
    Ведите строку в «верблюжьем регистре»:
    """
    for _ in text:
        if not _ == _.lower():
            text = text.replace(_, '_' + _.lower())
    return text[1:]

#   print(convert_to_python_case.__doc__)
print(convert_to_python_case(input()))




def get_middle_point(x1, y1, x2, y2):
    """
    Функция get_middle_point(x1, y1, x2, y2) принимает в качестве аргументов координаты концов отрезка (x1;y1) и (x2;y2)
    и возвращает координаты точки являющейся серединой данного отрезка.
    """    
    return (x1 + x2) / 2, (y1 + y2) / 2

print(*get_middle_point(int(input()), int(input()), int(input()), int(input())))




def get_middle_point(x1, y1, x2, y2):
    """
    Функция get_middle_point(x1, y1, x2, y2) принимает в качестве аргументов координаты концов отрезка (x1;y1) и (x2;y2)
    и возвращает координаты точки являющейся серединой данного отрезка.
    """    
    return (x1 + x2) / 2, (y1 + y2) / 2

x1, y1, x2, y2 = (int(input()) for _ in range(4))
x, y = get_middle_point(x1, y1, x2, y2)
print('Решением системы являются числа', 'x =', x, 'y =', y)



from math import pi

def get_circle(radius):
    """
    Функция get_circle(radius) принимает в качестве аргумента радиус окружности 
    и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
    """
    
    return 2 * pi * radius, pi * radius ** 2
    
length, square = get_circle(float(input()))
print(length, square)



from math import sqrt
def solve(a, b, c):
    """
    Функция поиска корней квадратного уравнения, при условии что D>=0
    """
    discr = b**2 - 4 * a * c
    if discr == 0: 
        x1 = x2 = -b / (2 * a)
    else:
        x1 = ((-b + sqrt(discr)) / (2 * a))
        x2 = ((-b - sqrt(discr)) / (2 * a))
    return min(x1, x2), max(x1, x2)

x1, x2 = solve(int(input()), int(input()), int(input()))
print(x1, x2)





import random

again = 'д'
while again.lower() == 'д':
    print('Бросаем кубики... ')
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (д = да, н = нет): ')





import random

for _ in range(10):
    num = random.randint(0, 1)
    if num == 0:
        print('Орел')
    else:
        print('Решка')







from math import *

print(ceil(log(int(input()), 2)))




import random

answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай',
           'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
           'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет',
           'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
           'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
while True:
    input("Задайте вопрос:")
    print("Происходит тряска магического шара...")
    n = random.randint(1, 20)
    for i in answers:
        if answers.index(i) == n:
            break
    print(i)
    question = input("Получили свой: yes или no?")
    if question == 'yes':
        break
print("Спасибо, что воспользовались услугами шара")




'''
# Шифр Цезаря

def cezar(text, n, lang):
    x = ''
    if lang == 'rus':  num_letters, low_letter, up_letter = 32, 'а', 'А'
    elif lang == 'eng':  num_letters, low_letter, up_letter = 26, 'a', 'A'
    for i in text:
        if i.islower(): 
            if i.isalpha(): x += chr(ord(low_letter) + (ord(i) - ord(low_letter) + num_letters + n) % num_letters)
        elif i.isupper():
            if i.isalpha(): x += chr(ord(up_letter) + (ord(i) - ord(up_letter) + num_letters + n) % num_letters)
        else: x += i  
    return x    

text, n, lang = input('Введите текст: '), int(input('Введите сдвиг - целое число: ')), input('Введите обозначение языка - rus или eng: ')
print(cezar(text, n, lang))




