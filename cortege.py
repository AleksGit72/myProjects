"""
Значения элементов кортежа невозможно изменить. 
При попытке изменить содержимое кортежа выдается ошибка TypeError.
"""
# Создание кортежа в Python
example = ('Earth', 'Venus', 'Mars')
print("ВЫВОД кортежа ('Earth', 'Venus', 'Mars'): ", example)
 
# Разные типы кортежей

# Пустой кортеж
my_tuple = ()
print(my_tuple)

# Кортеж с целыми числами
my_tuple = (1, 2, 3)
print(my_tuple)

# Кортеж с разными типами данных
my_tuple = (1, "Привет", 3.4)
print(my_tuple)

# Вложенный кортеж
my_tuple = ("мышь", [8, 4, 6], (1, 2, 3))
print(my_tuple)

"""
Слайсинг(сегментирование) кортежей:
СИНТАКСИС:
print(var[1:3], где 1-й включительно, 3-й - ИСКЛЮЧЕН!!!), 

Data:
   c   o   d   e   c   h   i   c   k
 0   1   2   3   4   5   6   7   8   9
-9  -8  -7  -6  -5  -4  -3  -2  -1
"""
my_tuple = ('c', 'o', 'd', 'e', 'c', 'h', 'i', 'c', 'k')
print("Кортеж для 'слайсинга': ", my_tuple)
# элементы со 2 по 4
# Вывод: ('o', 'd', 'e')
print("элементы со 2 по 4, Вывод: ('o', 'd', 'e'): ", my_tuple[1:4])

# элементы от начала и до второго элемента
# Вывод: ('c', 'o')
print("элементы от начала и до второго элемента, Вывод: ('c', 'o')",my_tuple[:-7])

# два последних элемента
# Вывод: ('c', 'k')
print("два последних элемента - my_tuple[7:] Вывод: ('c', 'k')", my_tuple[7:])

# все элементы от начала до конца
# Вывод: ('c', 'o', 'd', 'e', 'c', 'h', 'i', 'c', 'k')
print("все элементы от начала до конца - my_tuple[:]. Вывод: ('c', 'o', 'd', 'e', 'c', 'h', 'i', 'c', 'k')", my_tuple[:])
# END slising

# Конкатенация
#Вывод: (1, 2, 3, 4, 5, 6)
print("Конкатенация (1, 2, 3) + (4, 5, 6) - ", (1, 2, 3) + (4, 5, 6))

# Повторение
# Вывод: ('Повторить', 'Повторить', 'Повторить')
print("Повторение: ", ("Повторить",) * 3)

"""
Методы кортежа
Методы добавления или удаления элементов недоступны для кортежа в силу его неизменяемости. 
Для кортежа существует только два метода: .count() и .index(). 
"""
my_tuple = ('я', 'б', 'л', 'о', 'к', 'о',)

print(my_tuple.count('о'))  # Вывод: 2
print(my_tuple.index('к'))  # Вывод: 4

"""
Проверка на вхождение в кортеж
Мы можем проверить, существует ли тот или иной элемент в кортеже или нет, с помощью ключевого слова in и not in.
"""
my_tuple = ('я', 'б', 'л', 'о', 'к', 'о',)

print('я' in my_tuple) # Вывод: True
print('х' in my_tuple) # Вывод: Faulse
print('п' not in my_tuple) # Вывод: True

"""
Итерирование по кортежу
Для перебора элементов кортежа можно использовать цикл for. 
"""
for name in ('Андрей', 'Маша'):
    print("Привет, ", name) # Вывод: Привет, Андрей
                            # Вывод: Привет, Маша   

for sample in ('Bob', 'Kat', 'Sam'):
    print('Hi, dear ', sample)

# Удалить кортеж
x = (12, 13, 14, 15, 16)
#   print(var)
del x
print(x) # ВЫВОД:NameError: name 'var' is not defined
