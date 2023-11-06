# Создание глобальной переменной
example = "This is a trail"
def sample():
    print(example)
def second_sample():
    # Обращение из другой функции
    print(example)
sample()
second_sample()
num = int(input())
first_digit = num % 10
second_digit = (num % 100) // 10
third_digit = num // 100
c = str(first_digit)
b = str(second_digit)
a = str(third_digit)
print(int(a+b+c))
print(int(a+c+b))
print(int(b+a+c))
print(int(b+c+a))
print(int(c+a+b))
print(int(c+b+a))
