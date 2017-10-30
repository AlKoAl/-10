# Напишите программу, которая считывает текст состоящий одной строки
# и вычисляет сумму тех слов, которые являются числами.
Ar = [i for i in input().split()]
k = (len(Ar))
n = 0
for i in range(k):
    if Ar[i].isdigit():
        n = n + int(Ar[i])
print(n)