# Обращение к частям строки
first = 'Programming'
# Выводит всю строку
print('Example used = ', first)
# Выводит первый символ
print('first character = ', first[0])
# Выводит последний символ с помощью отрицательного
# индекса
print('last character = ', first[-1])
# Выводит последний символ с помощью положительного
# индекса
print('last character = ', first[10])
# Выводит срез от нулевого до третьего индекса
print('Sliced character = ', first[0:5])
example = 'This is ' + "''a great example''"*4
print(example)
# Додає при виводі наступну в кінець попередньої
example = "France is a beautiful country "
example += "you need to visit at least once"
example += " in the year."
print(example)
print(len(example))
sample = example.lower()
print(sample)
sample1 = example.upper()
print(sample1)
sample3 = example.title()
print(sample3) 