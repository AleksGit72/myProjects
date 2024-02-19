'''
# Пример функции с локальной переменной
def sample_local():
    example = "This is a trail" # локальная переменная, только для функции sample_local()
    print(example)
sample_local()

# Пример глобальной переменной
example = "This is a trail" # глобальная переменная
def first_sample():
    print(example) # Обращение из функции first_sample()
def second_sample():
    print(example) # Обращение из функции second_sample()
first_sample()
second_sample()

'''
def print_paris(): 
    s = 'I love Paris'
    print(s) 

def print_london():
    s = 'I love London'
    print(s) 

s = 'I love Kharkiv'
print_paris()
print_london()
print(s)



