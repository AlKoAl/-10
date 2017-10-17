# Задача № 2.
# Напишите программу вычисляющую произведение двух целых чисел.
# В программе гарантируется, что числа - целые. В программе запрещается использовать операцию *(умножить)
a = int(input())
c = a
b = int(input())
v = b
res = int(0)
import math
a = math.fabs(a)
b = math.fabs(b)
while (b > 0):
    if (b % 2 == 0):
        a = a + a
        b /= 2
    else:
        res = a + res
        b = b - 1
if c < 0:
    res *= -1
if v < 0:
    res *= -1
print (res)