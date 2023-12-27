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
"""
from math import factorial
num, s = int(input()), 0
for i in range(1, num + 1):
    s += factorial(i)
print(s)