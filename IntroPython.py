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


#  Форматирование вьівода

# простое форматирование:
x = 5; y = 10; z = 25 
print('Значение х = {}, а y = {}, но z = {}'.format(x,y,z))

# использование кортежа:
print('Я люблю {0} и {1}'.format('хлеб', 'масло'))
print('Я люблю {1} и {0}'.format('хлеб', 'масло'))

# Для форматирования строк можно использовать именованные аргументы. Вывод: Привет, Иван, доброго утра
print('Привет, {имя}, {пожелания}'.format(пожелания = 'доброго утра', имя = 'Иван'))


ind, res  = float(input()) / float(input()) ** 2, ['Недостаточная масса', 'Оптимальная масса', 'Избыточная масса']
if ind < 18.5:
    print(res[0])
elif ind > 25:
    print(res[2])
else:
    print(res[1])




res = len(input()) * 60
res1, res2 = res // 100, res % 100 
print(res1,'р.', res2, 'коп.')



print(len(input().split()))


# Кто ты по китайскому календарю
year, list =int(input('Введите Ваш год рождения: ')), ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
print('Вы -', list[year % 12], '(по китайскому календарю).')



#  Дано пятизначное или шестизначное натуральное число. Программа изменит порядок его последних пяти цифр на обратный(без незначащих нулей).
a = input()
print(int(a[::-1]) if len(a) == 5 else a[0] + a[:-6:-1])



print(f'{int(input()):,}')


#   Задача Иосифа Флавия:
#   n человек, пронумерованных числами от 1 до n, стоят в кругу. 
#   Они начинают считаться, каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
#   Программа определяет номер человека, который останется в кругу последним.

n, k, num = int(input()), int(input()), 0
for i in range(1, n + 1):
    num = (num + k) % i
print(num + 1)



#   Задача Иосифа Флавия:
#   n человек, пронумерованных числами от 1 до n, стоят в кругу. 
#   Они начинают считаться, каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
#   Программа определяет номер человека, который останется в кругу последним.

n = int(input())           # количество игроков
k = int(input())           # k-й по счету человек выбывает из круга
sp = list(range(1, n+1))   #создание списка с номерами 

while len(sp) > 1:         # Запуск цикла до тех пор, пока не останется один номер
    for i in range(k - 1): # Запуск цикла отсчета до удаляемого(убиваемого)
        tmp = sp.pop(0)    # Забираем из списка кто остается 
        sp.append(tmp)     # Переносим выжившего в конец списка, таким образом закольцовывая список  
    sp.pop(0)              # Удаление(убивание) того, кому не повезло
                           # И так по кругу пока не останется 1, номер которого выводим     

print(*sp)



#   Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
#   В первой строке записано количество точек. 
#   Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – x, затем ордината – y), разделенных символом пробела.
#   Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.
#   Точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти.

frst, scnd, thrd, frth = 0, 0, 0, 0
place = ['Первая четверть:', 'Вторая четверть:', 'Третья четверть:', 'Четвертая четверть:']
for _ in range(int(input())):
    xy = [int(_) for _ in input().split()]
    if xy[0] > 0 and xy[1] > 0: frst += 1
    elif xy[0] < 0 and xy[1] > 0: scnd += 1
    elif xy[0] < 0 and xy[1] < 0: thrd += 1
    elif xy[0] > 0 and xy[1] < 0: frth += 1
print(place[0], frst)
print(place[1], scnd)
print(place[2], thrd)
print(place[3], frth)


#   На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
#   Программа выводит одно число – количество случаев, когда следующий элемент списка больше предыдущего.

lst, count = [int(_) for _ in input().split()], 0
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        count +=1
print(count)




#   На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
#   Программа меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д., и после выводит его.
#   Если в списке нечетное количество элементов, то последний остается на своем месте

lst = [int(_) for _ in input().split()]
for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(*lst)




#   Программа циклического сдвига:
#   На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
#   Программа последний элемент ставит первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

lst = input().split()
lst.insert(0, lst.pop(-1))
print(*lst)


#   Программа циклического сдвига:
#   На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
#   Программа последний элемент ставит первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

lst = input().split()
new_lst = lst[-1:] + lst[:-1]
print(*new_lst)




#    Программа для определения, является ли введенное последнее число произведением двух чисел из введенного ранее набора (списка) чисел.
#    В первой строке подаётся число n (0<n<1000) – количество чисел в наборе.
#    В последующих n строках вводятся целые числа, составляющие набор (могут повторяться).
#    Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.
#    Программа выводит результат в виде ответа «ДА» или «НЕТ».

n = int(input())
lst = [int(input()) for i in range(n)]
trgt = int(input())
res = "НЕТ"
for i in range(0, n):
    if res == "ДА":
        break
    else:
        for j in range(0, n):
            if i!=j:
                if lst[i] * lst[j] == trgt:
                    res = "ДА"
                    break
print(res)




#    Программа для определения, является ли введенное последнее число произведением двух чисел из введенного ранее набора (списка) чисел.
#    В первой строке подаётся число n (0<n<1000) – количество чисел в наборе.
#    В последующих n строках вводятся целые числа, составляющие набор (могут повторяться).
#    Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.
#    Программа выводит результат в виде ответа «ДА» или «НЕТ».

n = int(input())
lst, trgt = [int(input()) for i in range(n)], int(input())
left, right = 0, len(lst) - 1
lst.sort()                               # сортируем список чисел по возрастанию
res = 'НЕТ'                              # делаем итоговый ответ равным НЕТ
while left != right:                     # пока указатели указывают на разные элементы списка
    if lst[left] * lst[right] > trgt:    # если произведение первого и последнего чисел в списке больше, чем число, которое проверяем
       right -= 1                        # сдвигаем правый указатель левее по списку
    elif lst[left] * lst[right] < trgt:  # иначе, если произведение первого и последнего чисел в списке меньше, чем число, которое проверяем
        left += 1                        # сдвигаем левый указатель правее по списку
    else:                                # во всех остальных случаях (произведение равно числу)
        res = 'ДА'                       # меняем итоговый ответ на ДА
        break                            # прерываем цикл досрочно

print(res)







#   Камень - ножницы - бумага
#   На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". 
#   На первой строке записан выбор Тимура, на второй – выбор Руслана.

t, r = input(), input()
win = ['каменьножницы', 'бумагакамень', 'ножницыбумага']
if t == r:
    print('ничья')
elif t + r in win:
    print('Тимур')
else:
    print ('Руслан')




#   Камень, ножницы, бумага, ящерица, Спок
#   На вход программе подаются две строки текста, содержащие слова "камень", "ножницы",  "бумага" , ящерица или Спок. 
#   На первой строке записан выбор Тимура, на второй – выбор Руслана.

t, r = input(), input()
win = ['каменьножницы', 'каменьящерица', 'ящерицаСпок', 'ящерицабумага', 'Спокножницы', 'Споккамень', 'бумагакамень', 'ножницыбумага', 'ножницыящерица', 'бумагаСпок']
if t == r:
    print('ничья')
elif t + r in win:
    print('Тимур')
else:
    print ('Руслан')



#   lst = 
print(len(max(input().split('О'))))




#   Кремниевая долина
#   Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
#   и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
#   то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы.
#   В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры.
#   Программа должна выводить номера зараженных холодильников через пробел. Если таких холодильников нет, ничего не выводится.

def is_grow(work_list):
    res = True
    for i in range(1, len(work_list)):
        if work_list[i] < work_list[i - 1]:
            res = False
            break
    return res

def find_hacker_name(src: str, pattern: str):
    work_list = []                            # лист индексов нужных букв из pattern тут "anton", src - строка в которой ищем буквы паттерна
    _ind = 0                                  # с какого индекса в src производить поиск. далее меняем
    for c in pattern:
        if c in src:
            work_list.append(src.find(c, _ind)) 
            _ind = work_list[-1]
    if len(work_list) == len(pattern):
        return is_grow(work_list)             # проверяет не убывающий ли массив индексов букв.
    return False

list_str = [input() for _ in range(int(input()))]
for i, s in enumerate(list_str, 1):
    if find_hacker_name(s, 'anton'):
        print(i, end=' ')



#   Кремниевая долина
#   Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
#   и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
#   то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы.
#   В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры.
#   Программа должна выводить номера зараженных холодильников через пробел. Если таких холодильников нет, ничего не выводится.

out = []
for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for el in s:
        if el == virus[x]:
            x += 1
        if x == 5:
            out.append(i + 1)
            break
print(*out)


#    2.2.11 Курс для продвинутых
#    Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста, а очередную строку отображает уже без этой буквы.
#    На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".
#    Программа должна вывести в соответствии с указанным алгоритмом строки, количество которых равно количеству разных букв в строке, которая получается путем конкатенации введенного слова и строки "запретил букву".

word = input() + ' запретил букву'
alph = [chr(_) for _ in range (1072, 1104) if chr(_) != 'ё']   # создаем список букв алфавита без 'ё'
for i in alph:                                                 # проходим по всему списку алфавита
    if i in word:                                              # если буква в есть в строке
        print(word, i)                                         # печатаем строку и букву, которую будем удалять
        word = word.replace(i, '').replace('  ', ' ').strip()  # удаляем/заменяем найденную букву на '', заменяем двойные пробелы на одинарные, удаляем пробелы в начале и конце строки




list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for el in list1:
   total += sum(el)
   counter += len(el)
print(total / counter)



my_list = [[1], [2, 3], [4, 5, 6]]
total = 0
for row in my_list:
    total += sum(row)
print(total)

#  4.3 Вложенные списки. Часть 2 шаг 8
#  На вход программе подается число n. Программа выводит построчно елементы созданного списка, состоящего из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(range(1, n + 1)))
print(*lst, sep='\n')


#  4.3 Вложенные списки. Часть 2 шаг 9
#  На вход программе подается число n. Программа выводит построчно елементы созданного списка, состоящего из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

n = int(input())
lst = []
for _ in range(1, n + 1):
    lst.append(list(range(1, _ + 1)))
print(lst)
print(*lst, sep="\n")



#  4.3 Вложенные списки. Часть 2 шаг 10
#  Треугольник Паскаля 1
#  На вход программе подается число n.
#  Программа должна вывести указанную строку треугольника Паскаля в виде списка.

from math import factorial

n = int(input())
n = int(input())
lst = [factorial(n) // (factorial(el) * factorial(n - el)) for el in range (n + 1)]
print(lst)


#  4.3 Вложенные списки. Часть 2 шаг 11
#  Треугольник Паскаля 1
#  На вход программе подается число n.
#  Программа должна вывести первые n строк треугольника Паскаля (в развернутом виде).

from math import factorial

n = int(input())
for i in range(0, n):
    lst = [factorial(i) // (factorial(el) * factorial(i - el)) for el in range(i + 1)]
    print(*lst)


#  4.3 Вложенные списки. Часть 2 шаг 12
#  Упаковка дубликатов 🌶️
#  На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
#  Программа должна вывести список, с упаковыванными в подсписки последовательности одинаковых символов заданной строки.


s = input().split()
res = [[s[0]]]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        res[-1].append(s[i])
    else:
        res.append([s[i]])
print(res)




#  4.3 Вложенные списки. Часть 2 шаг 13
#  Разбиение на чанки 🌶️
#  На вход программе подается две строки: на одной – символы, на другой – число n. Из первой строки формируется список.
#  Программа на базе функции chunked() (принимает на вход список и число, задающее длину чанка (куска), возвращает список из чанков)
#  выводит список с вложенными подсписками(чанками) длиной n 

def chunked(s, n):
    lst = []
    for i in range(0, len(s), n):
        lst.append(s[i:i + n])
    return lst

s, n = input().split(), int(input())
print(chunked(s, n))



#  4.3 Вложенные списки. Часть 2 шаг 14
#  Подсписки списка 🌶️🌶️
#  На вход программе подается строка текста, содержащая символы. Из данной строки формируется список.
#  Программа выводит список, содержащий все возможные подсписки списка, включая пустой список.

s, lst = input().split(), [[]]
n = len(s)
for i in range(1, n + 1):
    for j in range(n - i + 1):
        lst.append(s[j:j + i])
print(lst)

n, res = int(input()), 0
for _ in range(n):
    res += int(input())
print(res)
"""
import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(int(input('Введите число от 1 до 5 : '))))