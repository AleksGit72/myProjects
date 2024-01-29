"""
s = 'i Learn Python language'
print(s.capitalize())


s = input()
print('YES' if s == s.title() else 'NO')


print('YES' if input().lower().find('хорош') != -1 else 'NO')

"""
# подсчитывает количество буквенных символов в нижнем регистре.
s, count = input(), 0
for i in s:
    if i != i.upper():
        count += 1
print(count)


