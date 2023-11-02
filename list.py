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
print(x[1][2]) # output: 22
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
"""
Метод insert() 
СИНТАКСИС: имя_списка.insert(индекс, элемент)
"""
x = [32, 23, 12]
x.insert(2, 11)
print("x.insert(2, 11): елемент 11 вставлен на третью позицию списка [32, 23, 12], output: ", x)
"""
Метод sort():
СИНТАКСИС: 
sort()  - выстроить все элементы списка по возрастанию
sort(reverse = True)  - выстроить все элементы списка по убыванию.
"""
x = [23, 12, 11, 45]
x.sort()
print("выстроить все элементы списка [23, 12, 11, 45] по возрастанию", x)
x = ['USA', 'China', 'Russia', 'UK']
x.sort()
print("выстроить все элементы списка ['USA', 'China', 'Russia', 'UK'] по возрастанию",x)
x = [23, 12, 11, 45]
x.sort(reverse=True)
print("выстроить все элементы списка [23, 12, 11, 45] по убыванию", x)