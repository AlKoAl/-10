# Задача №1
#Напишите программу содержащую логическую функцию проверки списка чисел, на то составные ли они.
#Программа должна применять эту функцию к списку считанному с файла.
def prime(n):
    i = 2
    j = 0
    while i**2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if n == 1:
        print(n, 'Unite')
    else:
        if j == 1:
            print(n, 'Composite')
        else:
            print(n, 'Prime')
with open('text1.txt', 'r') as inf:
    s = inf.readline().strip().split()
    for k in range(len(s)):
         prime(int(s[k]))
