import random
from time import sleep
import datetime
import shutil


rus_power = 32
eng_power = 26
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lowercase_letters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_uppercase_letters = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
punctuation = "!#$%&*+-=?@^_"
current_hour = datetime.datetime.now().hour
allowed_commands = [
    "д",
    "y",
    "1",
    "н",
    "n",
    "2",
    "reset",
    "сброс",
    "3",
    "exit",
    "выход",
    "4",
]
modules = ["generator", "генератор", "encrypter", "шифратор"]
directions = ['enc', 'код', 'dec', 'декод']
username = ""
console_width, _ = shutil.get_terminal_size()


def print_separator(width, symbol):
    for _ in range(width):
        print(f"\033[32m\033[2m{symbol}", end="", flush=True)
        sleep(random.uniform(0, 0.02 * (67 / console_width)))
    print()


def print_title(width, title):
    print_separator(width, "=")
    str = (" ".join(title)).center(width)
    for i in range(len(str)):
        print(str[i], end="", flush=True)
        sleep(random.uniform(0, 0.02 * (67 / console_width)))
    print()
    print_separator(width, "=")
    print()


def print_passwords(str):
    for i in range(len(str)):
        print(str[i], end="", flush=True)
        sleep(random.uniform(0, 0.02 * (67 / console_width)))
    print()


def print_dots():
    for _ in range(2):
        print("\033[1m. ", end="", flush=True)
        sleep(0.5)
    print("\033[1m.", end="", flush=True)
    sleep(0.5)
    print("\r      \r\033[0m", end="")


def terminal_print(string):
    for i in range(len(string)):
        print(f"\033[32m\033[1m{string[i]}", end="", flush=True)
        if string[i] == " ":
            sleep(0.11)
        else:
            sleep(0.05)
    #    time.sleep(3)
    print("\033[0m")


def terminal_input(string):
    for i in range(len(string)):
        print(f"\033[32m\033[1m{string[i]}", end="", flush=True)
        if string[i] == " ":
            sleep(0.11)
        else:
            sleep(0.05)
    print()
    result = input("\033[7m > ")
    print("\033[0m\033[K", end="", flush=True)
    print_dots()
    return result


def print_error_message(string):
    if string == "unidentified":
        s1 = "неопознанная команда"
    elif string == "outofrange":
        s1 = "используемая команда неприменима в текущем окружении"
    elif string == "notanumber":
        s1 = "введенное выражение не является натуральным числом"
    elif string == "lessthat5":
        s1 = "длина пароля не должна быть меньше 5 символов"
    s = f"\033[1m\033[31mОшибка: {s1}! Пожалуйста, повторите ввод."
    for c in s:
        print(c, end="", flush=True)
        if c == " ":
            sleep(0.12)
        else:
            sleep(0.05)
    print("\033[0m")


def is_invalid_number(s):
    if not s.isdigit():
        if s in (["д", "н", "y", "n"] + modules + directions):
            return "outofrange"
        elif s in ["reset", "exit", "сброс", "выход"]:
            return ""
        else:
            return "notanumber"
    else:
        if s == "0":
            return "notanumber"
        else:
            return ""


def is_short_length(s):
    if s.isdigit() and int(s) < 5:
        return "lessthat5"
    else:
        return ""


def execute_command(s):
    if s == "reset":
        terminal_print(f"Принято, {username}. Перезапускаю программу...")
        sleep(1)
    elif s == "exit":
        terminal_print(f"Принято, {username}. Завершаю работу программы...")
        print()
        print_separator(console_width, "=")
        print()
    elif s == "generator":
        terminal_print(
            f'Принято, {username}. Обращаюсь к модулю "Генератор надежных паролей"...'
        )
    elif s == "encrypter":
        terminal_print(
            f'Принято, {username}. Обращаюсь к модулю "Шифратор/дешифратор"...'
        )


def remove_ambiguous(lst):
    for i in range(len(lst)):
        for c in "iloIO10":
            lst[i] = lst[i].replace(c, "")
    return lst


def loading():
    print("\033[32m", end="")
    for i in range(21):
        print(" ", 5 * i, "%\t", (i // 2) * "##", sep="", end="\r")
        sleep(random.uniform(0.3, 1))
    print("\n\033[0m")


def generate_password(length, alphabet, amount):
    variety = [0] * amount
    password = list()
    while sum(variety) != length:
        variety = [0] * amount
        for i in range(amount):
            variety[i] = random.randint(1, length - amount + 1)  # + i - sum(variety))
    random.shuffle(variety)
    for i in range(amount):
        for _ in range(variety[i]):
            password.append(random.choice(alphabet[i]))
    random.shuffle(password)
    return "".join(password)


def run_password_generator():
    print_title(console_width, "ГЕНЕРАТОР НАДЕЖНЫХ ПАРОЛЕЙ")
    sleep(1)
    terminal_print(f'{username}, Вы используете модуль "Генератор надежных паролей".')
    sleep(1)
    terminal_print(
        "Целью данной подпрограммы является генерация заданного количества паролей одинаковой длины из определенного набора символов."
    )
    sleep(1)
    terminal_print("Задать указанные параметры Вы сможете через терминал.")
    sleep(1)
    terminal_print(
        "Длина и количество паролей должны быть определены в виде натуральных чисел."
    )
    sleep(1)
    terminal_print(
        'Для ответа на вопросы программы используйте символы "Y" или "Д" (утвердительный ответ) и "N" или "Н" (отрицательный ответ).'
    )
    sleep(1)
    terminal_print(
        'Чтобы сбросить введенные данные и начать генерацию паролей заново, используйте команду "RESET" или "СБРОС".'
    )
    sleep(1)
    terminal_print('Чтобы выйти из модуля, используйте команду "EXIT" или "ВЫХОД".')
    sleep(1)
    print()

    while True:
        command = terminal_input(
            "Желаете продолжить работу?\n\t1) YES\n\t2) NO\n\t3) EXIT"
        ).lower()
        if command not in allowed_commands or command == "4":
            print_error_message("unidentified")
        elif command in (allowed_commands[6:8] + modules + directions):
            print_error_message("outofrange")
        else:
            break
    if command in allowed_commands[3:6] or command in allowed_commands[8:11]:
        execute_command("exit")
    else:

        while True:
            length = 0
            alphabet = list()
            amount = 0
            passwords = list()

            print()
            print_separator(console_width, "=")
            print()
            while True:
                number_of_passwords = terminal_input(
                    "Введите количество генерируемых паролей:"
                ).lower()
                error_code = is_invalid_number(number_of_passwords)
                if error_code:
                    print_error_message(error_code)
                else:
                    break
            if number_of_passwords in allowed_commands[6:8]:
                execute_command("reset")
                continue
            elif number_of_passwords in allowed_commands[9:11]:
                execute_command("exit")
                break
            else:
                number_of_passwords = int(number_of_passwords)
            print()

            while True:
                length = terminal_input(
                    "Введите длину одного пароля (не менее 5 символов):"
                ).lower()
                error_code = is_invalid_number(length) + is_short_length(length)
                if error_code:
                    print_error_message(error_code)
                else:
                    break
            if length in allowed_commands[6:8]:
                execute_command("reset")
                continue
            elif length in allowed_commands[9:11]:
                execute_command("exit")
                break
            else:
                length = int(length)
            print()

            while True:
                command = terminal_input(
                    "Включить прописные буквы (ABC...)?\n\t1) YES\n\t2) NO\n\t3) RESET\n\t4) EXIT"
                ).lower()
                if command not in allowed_commands:
                    if command in (modules + directions):
                        print_error_message("outofrange")
                    else:
                        print_error_message("unidentified")
                else:
                    break
            if command in allowed_commands[:3]:
                alphabet.append(uppercase_letters)
            elif command in allowed_commands[6:9]:
                execute_command("reset")
                continue
            elif command in allowed_commands[9:]:
                execute_command("exit")
                break
            print()

            while True:
                command = terminal_input(
                    "Включить строчные буквы (abc...)?\n\t1) YES\n\t2) NO\n\t3) RESET\n\t4) EXIT"
                ).lower()
                if command not in allowed_commands:
                    if command in (modules + directions):
                        print_error_message('outofrange')
                    else:
                        print_error_message("unidentified")
                else:
                    break
            if command in allowed_commands[:3]:
                alphabet.append(lowercase_letters)
            elif command in allowed_commands[6:9]:
                execute_command("reset")
                continue
            elif command in allowed_commands[9:]:
                execute_command("exit")
                break
            print()

            while True:
                command = terminal_input(
                    "Включить цифры?\n\t1) YES\n\t2) NO\n\t3) RESET\n\t4) EXIT"
                ).lower()
                if command not in allowed_commands:
                    if command in (modules + directions):
                        print_error_message('outofrange')
                    else:
                        print_error_message("unidentified")
                else:
                    break
            if command in allowed_commands[:3]:
                alphabet.append(digits)
            elif command in allowed_commands[6:9]:
                execute_command("reset")
                continue
            elif command in allowed_commands[9:]:
                execute_command("exit")
                break
            print()

            while True:
                command = terminal_input(
                    "Включить специальные символы (!#$...)?\n\t1) YES\n\t2) NO\n\t3) RESET\n\t4) EXIT"
                ).lower()
                if command not in allowed_commands:
                    if command in (modules + directions):
                        print_error_message('outofrange')
                    else:
                        print_error_message("unidentified")
                else:
                    break
            if command in allowed_commands[:3]:
                alphabet.append(punctuation)
            elif command in allowed_commands[6:9]:
                execute_command("reset")
                continue
            elif command in allowed_commands[9:]:
                execute_command("exit")
                break
            print()

            while True:
                command = terminal_input(
                    "Исключить неоднозначные символы (ilI1oO0)?\n\t1) YES\n\t2) NO\n\t3) RESET\n\t4) EXIT"
                ).lower()
                if command not in allowed_commands:
                    if command in (modules + directions):
                        print_error_message('outofrange')
                    else:
                        print_error_message("unidentified")
                else:
                    break
            if command in allowed_commands[:3]:
                alphabet = remove_ambiguous(alphabet)
            elif command in allowed_commands[6:9]:
                execute_command("reset")
                continue
            elif command in allowed_commands[9:]:
                execute_command("exit")
                break
            print()

            amount = len(alphabet)

            if length < 8 or amount < 3:
                terminal_print(
                    "Считаю необходимым заметить, что для большей надежности пароль должен состоять не менее, чем из 8 символов, и содержать не менее 3 видов символов."
                )
                sleep(1)
                print()
                print_dots()
            terminal_print("Данные приняты в обработку.")
            sleep(1)
            terminal_print("Программа выполняется, пожалуйста, подождите...\n")
            loading()

            if number_of_passwords == 1:
                ending = "я"
            else:
                ending = "ей"
            terminal_print(f"Генерация парол{ending} прошла успешно, {username}!")
            print()

            for _ in range(number_of_passwords):
                passwords.append(generate_password(length, alphabet, amount))

            print_separator(console_width, "*")
            str_password = ""
            for i in range(len(passwords)):
                # str_length = len(str_password)
                if (
                    len(str_password) // (length + 4)
                    >= console_width // (length + 4) - 1
                ):
                    str_password += passwords[i]
                    str_length_mem = len(str_password)
                    print_passwords(str_password.center(console_width))
                    str_password = ""
                    continue
                else:
                    str_password += passwords[i] + "    "
                    str_length_mem = len(str_password)

            str_password += " " * (str_length_mem - len(str_password))
            print(str_password.center(console_width))
            print_separator(console_width, "*")
            print()

            sleep(1)
            while True:
                command = terminal_input(
                    "Желаете продолжить работу?\n\t1) YES\n\t2) NO\n\t3) RESET\n\t4) EXIT"
                ).lower()
                if command not in allowed_commands:
                    print_error_message("unidentified")
                    continue
                else:
                    break
            if command in allowed_commands[:3] + allowed_commands[6:9]:
                execute_command("reset")
                continue
            elif command in allowed_commands[3:6] + allowed_commands[9:]:
                execute_command("exit")
                break

def caesar_encoding(symbol, step, alphabet, power):
    index = alphabet.find(symbol)
    code_index = (index + step) % power
    return alphabet[code_index]

def run_encrypter():
    print_title(console_width, "ШИФРАТОР/ДЕШИФРАТОР")
    sleep(1)
    terminal_print(f'{username}, Вы используете модуль "Шифратор/дешифратор".')
    sleep(1)
    terminal_print(
        "Целью данной подпрограммы является кодирование или декодирование заданного текстового сообщения на русском или английском языке с помощью шифра Цезаря."
    )
    sleep(1)
    terminal_print(
        "Шаг сдвига для кодирования/декодирования задается вручную в виде натурального числа."
    )
    sleep(1)
    terminal_print(
        'Чтобы задать направление, используйте команды "ENC" или "КОД" (шифрование) и "DEC" или "ДЕКОД" (дешифрование).'
    )
    sleep(1)
    print()

    while True:
        command = terminal_input(
            "Желаете продолжить работу?\n\t1) YES\n\t2) NO\n\t3) EXIT"
        ).lower()
        if command not in allowed_commands or command == "4":
            print_error_message("unidentified")
        elif command in allowed_commands[6:8] or command in modules:
            print_error_message("outofrange")
        else:
            break
    if command in allowed_commands[3:6] or command in allowed_commands[8:11]:
        execute_command("exit")
    else:
       
        while True:
            encoded_message = ''
           
            print()
            print_separator(console_width, "=")
            print()
           
            message = terminal_input('Введите исходное сообщение:')
            if 'Ё' in message or 'ё' in message:
                terminal_print('Внимание: текст содержит букву "ё". В целях осуществления кодирования/декодирования она будет заменена на "е".')
                sleep(1)
                while 'Ё' in message:
                    message = message.replace('Ё', 'Е')
                while 'ё' in message:
                    message = message.replace('ё', 'е')
            print()           

            while True:
                direction = terminal_input('Выберите режим работы (кодирование/декодирование):\n\t1) ENCODE\n\t2) DECODE\n\t3) RESET\n\t4) EXIT').lower()
                if direction not in (directions + allowed_commands[5:] + ['1']):
                    if direction in (modules + allowed_commands[:5]):
                        print_error_message('outofrange')
                    else:
                        print_error_message('unidentified')
                else:
                    break
            if direction in (directions[:2] + ['1']):
                sign = 1
                prefix = ''
            elif direction in (directions[2:] + ['2']):
                sign = -1
                prefix = 'де'
            elif direction in allowed_commands[6:9]:
                execute_command('reset')
                continue
            else:
                execute_command('exit')
                break
            print()           

            while True:
                step = terminal_input(f'Введите шаг сдвига для {prefix}кодирования:').lower()
                error_code = is_invalid_number(step)
                if error_code:
                    print_error_message(error_code)
                else:
                    break
            if not step.isdigit():
                if step in allowed_commands[6:8]:
                    execute_command('reset')
                    continue
                else:
                    execute_command('exit')
                    break
            else:
                step = int(step) * sign
            print()
           
            terminal_print("Данные приняты в обработку.")
            sleep(1)
            terminal_print("Программа выполняется, пожалуйста, подождите...\n")
            loading()
           
            encoded_message = ''
            for symbol in message:
                if symbol in lowercase_letters:
                    new_symbol = caesar_encoding(symbol, step, lowercase_letters, eng_power)
                elif symbol in uppercase_letters:

                    new_symbol = caesar_encoding(symbol, step, uppercase_letters, eng_power)
                elif symbol in rus_lowercase_letters:
                    new_symbol = caesar_encoding(symbol, step, rus_lowercase_letters, rus_power)
                elif symbol in rus_uppercase_letters:
                    new_symbol = caesar_encoding(symbol, step, rus_uppercase_letters, rus_power)
                else:
                    new_symbol = symbol
                encoded_message += new_symbol

            terminal_print(f"{(prefix + 'кодирование').capitalize()} сообщения прошло успешно, {username}!")
            print()
            print_separator(console_width, "*")
            print_passwords(encoded_message.center(console_width))
            print_separator(console_width, "*")
            print()

            sleep(1)
            while True:
                command = terminal_input(
                    "Желаете продолжить работу?\n\t1) YES\n\t2) NO\n\t3) RESET\n\t4) EXIT"
                ).lower()
                if command not in allowed_commands:
                    print_error_message("unidentified")
                    continue
                else:
                    break
            if command in allowed_commands[:3] + allowed_commands[6:9]:
                execute_command("reset")
                continue
            elif command in allowed_commands[3:6] + allowed_commands[9:]:
                execute_command("exit")
                break

print_title(console_width, "СИСТЕМА БЕЗОПАСНОСТИ VAULT-TEC")
sleep(1)

username = terminal_input("Пожалуйста, введите имя пользователя:").title()

terminal_print("Авторизация прошла успешно!")
sleep(1)

if 4 <= current_hour <= 5:
    hello = (
        f"Доброе утро, {username}! Ваше появление в столь ранний час весьма неожиданно."
    )
    goodbye = f"Хорошего дня, {username}! Надеюсь, что раннее пробуждение не скажется на Вашей активности!"
elif 6 <= current_hour < 12:
    hello = f"Доброе утро, {username}!"
    goodbye = f"Хорошего дня, {username}!"
elif 12 <= current_hour < 17:
    hello = f"Добрый день, {username}!"
    goodbye = f"Хорошего дня, {username}!"
elif 17 <= current_hour < 23:
    hello = f"Добрый вечер, {username}!"
    if current_hour <= 20:
        goodbye = f"До свидания, {username}!"
    else:
        goodbye = f"Доброй ночи, {username}!"
else:
    hello = f"Здравствуйте, {username}! Довольно позднее время Вы выбрали для работы."
    goodbye = f"Доброй ночи, {username}! Позволю себе напомнить Вам, что позднее засыпание может негативно сказаться на продуктивности труда."

print()
terminal_print(hello)
sleep(1)
terminal_print("Вас приветствует система безопасности Vault-Tec.")
sleep(1)
terminal_print(
    "В функциональные модули программы входят генератор надежных паролей и шифратор/дешифратор."
)
sleep(1)
terminal_print(
    "Взаимодействие с программой осуществляется посредством использования определенного набора команд, которые могут различаться в зависимости от модуля."
)
sleep(1)
terminal_print(
    'Чтобы перейти к подпрограмме "Генератор надежных паролей", введите команду "GENERATOR" или "ГЕНЕРАТОР".'
)
sleep(1)
terminal_print(
    'Чтобы перейти к подпрограмме "Шифратор/дешифратор", введите команду "ENCRYPTER" или "ШИФРАТОР".'
)
sleep(1)
terminal_print('Чтобы выйти из программы, используйте команду "EXIT" или "ВЫХОД".')
sleep(1)
print()

while True:
    module = terminal_input(
        f"Какой модуль Вы желаете запустить, {username}?\n\t1) GENERATOR\n\t2) ENCRYPTER\n\t3) EXIT"
    ).lower()
    if module not in (modules + allowed_commands[8:11] + ['1', '2']):
        if module in (allowed_commands[:8] + directions):
            print_error_message("outofrange")
        else:
            print_error_message("unidentified")
    else:
        if module in modules[:2] + ['1']:
            execute_command("generator")
            print()
            sleep(1)
            print_dots()
            run_password_generator()
        elif module in modules[2:] + ['2']:
            execute_command("encrypter")
            print()
            sleep(1)
            run_encrypter()
        elif module in allowed_commands[8:11]:
            execute_command("exit")
            break
    sleep(1)

sleep(1)
terminal_print("Работа программы завершена.")
sleep(1)
terminal_print(goodbye)
print("\033[32m", end="")