"""
# Шифр Цезаря

def cezar(text, n, lang):
    x = ''
    if lang == 'rus':  num_letters, low_letter, up_letter = 32, 'а', 'А'
    elif lang == 'eng':  num_letters, low_letter, up_letter = 26, 'a', 'A'
    for i in text:
        if i.islower(): 
            if i.isalpha(): x += chr(ord(low_letter) + (ord(i) - ord(low_letter) + num_letters + n) % num_letters)
        elif i.isupper():
            if i.isalpha(): x += chr(ord(up_letter) + (ord(i) - ord(up_letter) + num_letters + n) % num_letters)
        else: x += i  
    return x    

text, n, lang = input('Введите текст: '), int(input('Введите сдвиг - целое число: ')), input('Введите обозначение языка - rus или eng: ')
print(cezar(text, n, lang))






"""

#  На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
#  Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
#  Строчные буквы при этом остаются строчными, а прописные – прописными.
#  Гарантируется, что между различными словами присутствует один пробел.


def cezar(text, n):  #  функция шифрования  строки text co сдвигом n
    x = ""
    for i in text:
        if not i.isalpha():
            x += i
        elif i.islower():
            x += chr(ord("a") + (ord(i) - ord("a") + 26 + n) % 26)
        else:
            x += chr(ord("A") + (ord(i) - ord("A") + 26 + n) % 26)
    return x


def text_len(text):  # функция определения длины слова без учета символов (только буквы)
    count = 0
    for el in text:
        if el.isalpha():
            count += 1
    return count


text = (cezar(el, text_len(el)) for el in input().split(" "))
print(*text)
