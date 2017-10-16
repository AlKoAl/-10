# задача 1
# Напишите программу вычисляющую результат остатка при делении a^b на c.
# В программе гарантируется, что числа a и c целые, b - натуральное и не превосходят по модулю 10000.
# В программе запрещается использовать операцию **(возведение в степень).
# Результаты всех промежуточных вычислений не должны превосходить 100000000.
a = int(input())
b = int(input())
if b <= 0:
    print (' Введите новое число')
c = int(input())
if c == 0:
    print (' Введите новое число')
    c = int(input())
if a > 0 and c > 0:
    d = a % c
    while b > 0:
        d = d % c
        d = d * a
        b = b - 1
if a > 0 and c < 0:
    c = -c
    d = a % c
    while b >0:
        d = d % c
        d = d * a
        b = b - 1
if a < 0 and c > 0:
    if b % 2 == 0:
        a = -a
        d = a % c
        while b > 0:
            d = d % c
            d = d * a
            b = b - 1
    else:
        if (-a)%(c) == 0:
            d = 0
        else:
            k = (-a) // c
            d = a - (-k - 1) * c
            while b > 0:
                d = d % c
                d = d*(-a)
                b = b - 1
if a<0 and c<0:
    if (-a)%c == 0:
        d = 0
    else:
        while b > 0:
            k = (-a) // (-c)
            d = a - (k + 1) * c
            while b >0:
                d = d % (-c)
                d = (-a) * d
                b = b - 1
import math
a = math.fabs(a)
d = d / a
print (int(d))