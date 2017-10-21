# задача № 2
# Напишите программу вычисляющую минимум, максимум и среднее арифметическое элементов массива,
# введенного из консоли.
n = int(input())
s = 0
k = 0
a = [0 for i in range(n)]
for i in range(n):
    a[i] = int(input())
min = min(a)
max = max(a)
for i in range(n):
    s = s + a[i]
    k = k+1
avg = s/k
print('min:',min)
print('max:',max)
print('avg:',avg)
