# a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5 , числа a,b,c,d,e < 150

"""
total = 0
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                for e in range(d, 151):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5 and e ** 5 > d ** 5 > c ** 5 > b ** 5 > a ** 5:
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e, 'sum = ', a + b + c + d + e)                    
                        total += 1
                        break
                        #  if  e ** 5 > d ** 5 > c ** 5 > b ** 5 > a ** 5:
print('Общее количество натуральных решений =', total)
"""
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(sum ** (1/5)) # отсекаем дробную часть !!!
                if sum == e ** 5:
                    print(a, b, c, d, e)
                    print(a + b + c + d + e)
                    break