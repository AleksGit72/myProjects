"""
a = int(input())
print(bin(a)[2:])

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:13])

# Программа должна вывести «YES», если слово является палиндромом, и «NO» в противном случае.
s = input()
if s == s[::-1]:
    print('YES')
else:
    print('NO')


# Программа должна вывести «YES», если слово является палиндромом, и «NO» в противном случае.
s = input()
print('YES' if s==s[::-1] else 'NO')


# put your python code here
#общее количество символов в строке;
#исходную строку, повторенную 3 раза;
#первый символ строки;
#первые три символа строки;
#последние три символа строки;
#строку в обратном порядке;
#строку с удаленным первым и последним символом.
s = input()
print(len(s), s*3, s[:1], s[:3], s[-3:], s[::-1], s[1:-1], sep = "\n" )

"""

# put your python code here
#третий символ этой строки;
#предпоследний символ этой строки;
#первые пять символов этой строки;
#всю строку, кроме последних двух символов;
#все символы с четными индексами;
#все символы с нечетными индексами;
#все символы в обратном порядке;
#все символы строки через один в обратном порядке, начиная с последнего
s = input()
print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2], sep = "\n")
