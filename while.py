"""
num = int(input())
while num%7 != 0:
    print(num)
    num = int(input())

#  цифровой корень числа
num_core = int(input()) 
while num_core > 9:
    s = 0
    while num_core > 0:
        s += num_core % 10
        num_core = num_core // 10
    num_core = s
print(num_core)

# факториал числа
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)

from math import factorial
num, s = int(input()), 0
for i in range(1, num + 1):
    s += factorial(i)
print(s)

a, b = int(input()), int(input())    # Считываем числа и записываем их в переменные a, b
for i in range(a, b + 1):    # Создаем внешний цикл 'i' от a до b включительно
    counter = 0    # Создаем счетчик counter = 0
    for j in range(1, i / 2 + 1):    # Создаем внутренний цикл от 1 до 'i' включительно
        if i % j == 0:    # Задаем условие если 'i' % 'j' == 0
            counter += 1    # Счетчик +1
    if counter == 2:    # Теперь на равне с внутренним циклом создаем условие для проверки, (простое число делится на единицу и на себя следовательно счетчик должен быть равен 2-м) если счетчик равен 2
        print(i)    # Выводим те самые числа


s = str(input())
total = 0 
for i in range(len(s)):
    total += int(s[i])
print(total)


"""

x, p, s = input(), 0, 0
for i in x:
    if i == "+":
        p += 1
    elif i == "*":
        s += 1
print("Символ + встречается", p, "раз")
print("Символ * встречается", s, "раз")
print(x)
