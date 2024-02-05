"""
s = 'i Learn Python language'
print(s.capitalize())


s = input()
print('YES' if s == s.title() else 'NO')


print('YES' if input().lower().find('хорош') != -1 else 'NO')


# подсчитывает количество буквенных символов в нижнем регистре.
s, count = input(), 0
for i in s:
    if i != i.upper():
        count += 1
print(count)


s = input().lower()
print('Аденин: ' + str(s.count('а')), 'Гуанин: ' + str(s.count('г')), 'Цитозин: '+ str(s.count('ц')), 'Тимин: ' + str(s.count('т')), sep = '\n')


n, count = int(input()), 0
for _ in range(n):
    if input().count('11') >= 3:
        count +=1
print(count)

# подсчитывает количество цифр в строке.
s, count = input(), 0
for i in s:
    if i in '0123456789':
        count += 1
print(count)

# подсчитывает количество цифр в строке.
s, total = input(), 0
for i in range(10):
    total += s.count(str(i))
print(total)

s = input()
print('YES' if s.endswith(('.com', '.ru')) else 'NO')


# выводит на экран символ, который появляется наиболее часто, если таких символов несколько, следует вывести последний по порядку символ.
s, count, n = input(), 0, 0
for i in s:
    n = s.count(i)
    if n >= count:
        count = n
        letter = i
print(letter)



s = input()
n = s.count('f')
if n == 1:
    print(s.find('f'))
elif n > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')


s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])

s = '    abbc    '
print(s.isspace())


first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print('Hello, {0} {1}. You are {2}. You are a {3}. You were a member of {4}'
               .format(first_name, last_name, age, profession, affiliation))


s = 'In {}, someone paid {} {} for two pizzas.'
year, value, money = '2010', '10k', 'Bitcoin'
print(s.format(year, value, money))

"""
year = 2010
amount = '10K'
currency = 'Bitcoin'
print(f'In {year}, someone paid {amount} {currency} for two pizzas.')