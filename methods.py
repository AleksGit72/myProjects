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
"""
s = input()
print('YES' if s.endswith(('.com', '.ru')) else 'NO')