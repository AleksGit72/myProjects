"""
for i in range(26):
    print(chr(ord('A') + i))

"""




# Шифр Цезаря, декодировать сообщение
shift, code_message = int(input()), input()
for i in code_message:
    if ord(i) - shift  < 97:
        print(chr(ord(i) - shift + 26), end='')
    else:
        print(chr(ord(i) - shift), end='')
