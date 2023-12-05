# break, continue, else

"""
#  программa, которая определяет, содержит ли введенное пользователем число цифру 7:
num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    num //= 10
if flag:  # эквивалентно if flag == True:
    print('Число', number, 'содержит цифру 7')
else:
    print('Число', number, 'не содержит цифру 7')


mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)

n = int(input()) # Программа должна вывести наименьший делитель инпута отличный от 1
for i in range(2, n+1):
    if n % i == 0:
        break
print(i)

n = int(input())
for i in range(1, n+1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue   
print(i)

n = int(input())
for i in range(1, n +1):
    for j in range(1, n + 1):
        print(i, end='')
    print()

"""
n = int(input())
total = 1
for i in range(1, n + 1):
    # print(i, end=" ")
    for j in range(0, i):
        print(total, end=' ')
        total += 1
    print()