'''
# Пример функции с локальной переменной
def sample_local():
    example = "This is a trail" # локальная переменная, только для функции sample_local()
    print(example)
sample_local()

# Пример глобальной переменной
example = "This is a trail" # глобальная переменная
def sample():
    print(example)
def second_sample():
    # Обращение из другой функции
    print(example)
sample()
second_sample()

'''

