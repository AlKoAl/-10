# Напишите программу считывающую массив чисел из строки
# и выписывающую в обратном порядке все числа стоящие на четных позициях.
Ar = [int(i) for i in input().split()]
n = (len(Ar))
Br = []
for i in range(n):
    if i % 2 != 0:
        Br.append(Ar[i])
k = len(Br)
Cr = []
for i in range(k):
    Cr.append(str(Br[k-(i+1)]))
Dr = ' '.join(Cr)
print(Dr)