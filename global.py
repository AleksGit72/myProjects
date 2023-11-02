# Создание глобальной переменной
example = "This is a trail"
def sample():
    print(example)
def second_sample():
    # Обращение из другой функции
    print(example)
sample()
second_sample()