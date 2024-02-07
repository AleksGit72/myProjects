"""
# списки
sample = ['Nevada', 'Ohio', 'Colorado']
print(sample)
print(sample[0])
print(sample[1])
print(sample[2])
print(sample[2] + ' is a great city')
print(sample[-1])

# вложенньіе списки
x = [[1, 223], [245, 63, 22]]
print(x[1][0]) # output: 245(0-й елемент підсписку 1)

# срез списка
sample = [12, 32, 21, 24, 65]
print("срез списка", sample[:2])

# конкатенация + дублирование списка
sample = [12, 32, 21, 24, 65]
example = [11, 22, 33]
print(sample*3 + example)

# Операторы логические: in и not in
print('Football' in ['Cricket', 'Football', 'Hockey']) # output: TRUE

# удаление елемента
sample = [2, 3, 4, 6, 8]
del sample[2]
print(sample) # output : [2, 3, 6, 8]

# Метод index() - найти индекс элемента в списке.
x = [32, 23, 12]
print("индекс элемента 23 в списке [32, 23, 12]: ", x.index(23)) # output: 1
# print("индекс элемента 55 в списке [32, 23, 12]: ", x.index(55)) # output: ValueError: 55 is not in list

#Метод insert() 
#СИНТАКСИС: имя_списка.insert(индекс, элемент)
x = [32, 23, 12]
x.insert(2, 11)
print("x.insert(2, 11): елемент 11 вставлен на третью позицию списка [32, 23, 12], output: ", x)

Метод sort():
СИНТАКСИС: 
sort()  - выстроить все элементы списка по возрастанию
sort(reverse = True)  - выстроить все элементы списка по убыванию.

x = [23, 12, 11, 45]
x.sort()
print("выстроить все элементы списка [23, 12, 11, 45] по возрастанию", x)

x = ['USA', 'China', 'Russia', 'UK']
x.sort()
print("выстроить все элементы списка ['USA', 'China', 'Russia', 'UK'] по возрастанию",x)

x = [23, 12, 11, 45]
x.sort(reverse=True)
print("выстроить все элементы списка [23, 12, 11, 45] по убыванию", x)



print(list(chr(x) for x in range(97, 97 + int(input()))))


numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(max(numbers) + min(numbers))


evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)


rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3, -1] = 'Зеленый', 'Фиолетовый'
print(rainbow)


languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
languages.reverse()
print(languages)


languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])



numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
print(numbers1 * 2 + numbers2 * 9 + numbers3)



numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers), numbers[-1], numbers[::-1], 'YES' if 5 and 17 in numbers else 'NO', numbers[1:-1], sep='\n')


n = int(input()) # На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных строк список и выводит его.
ls = []
for _ in range(n):
    ls.append(input())
print(ls)

# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных строк список и выводит его.
print([input() for _ in range(int(input()))]) 

# выводит следующий список:['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', .. Z * 26]
print([chr(i) * (i - 96) for i in range(97, 123)]) 


# На вход программе подаются натуральное число n, а затем n целых чисел. Программа выводит  список, состоящий из кубов введенных чисел
print([int(input()) ** 3 for _ in range(int(input()))]) 


#  программа создает список, состоящий из делителей введенного числа. v1
n = int(input())
list = [1]
for i in range (2, n // 2 + 1):
    if n % i == 0:
        list.append(i)
list.append(n)
print(list)

#  программа создает список, состоящий из делителей введенного числа.
n = int(input())
print([1] + [i for i in range(2, n // 2 + 1) if n % i == 0] + [n])



# На вход программе подаются натуральное число n, а затем n целых чисел. Программа выводит  список, состоящий из сумм соседних чисел
lst = [input() for _ in range(int(input()))]
print([int(lst[i] + lst[i + 1]) for i in range(len(lst) - 1)])


# На вход программе подаются натуральное число n, а затем n целых чисел. Программа удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.
lst = [int(input()) for _ in range(int(input()))]
del lst[1::2]
print(lst)

# На вход программе подаются натуральное число n, а затем n целых чисел. Программа удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.
lst = [int(input()) for _ in range(int(input()))]
print([lst[0]] + [lst[i] for i in range(2,len(lst),2)])

# На вход программе подаются натуральное число n, а затем n целых чисел. Программа удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.
print([int(input()) for _ in range(int(input()))][0::2])

# На вход программе подается натуральное число n,  далее n строк, каждая на отдельной строке. В конце вводится натуральное число k – номер буквы (нумерация начинается с единицы).
# Программа должна вывести текст: k-ую букву из введенных строк на одной строке без пробелов..
# ВАЖНО: Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе нужно игнорировать.
lst = [input() for _ in range(int(input()))]
k = int(input())
for i in range(len(lst)):
    if len(lst[i]) >= k:
        print(lst[i][k - 1], end='')



k, lst = int(input()), []
for _ in range(k):
    lst.extend(input())
print(lst)


lst = []
print([lst.extend(input()) for _ in range(int(input()))])
"""

