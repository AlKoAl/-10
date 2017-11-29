# Задача №2
# Напишите программу, содержащую функцию вычисляющую функцию Эйлера для произвольного натурального числа.
# Программа должна считывать из файла массив чисел и находить среднее геометрическое значений функции
# Эйлера чисел массива
def prime(n):
    i = 2
    j = 0
    while i**2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if j != 1:
        return(n)
    else:
        return('none')
def elier_funk(n):
    A = []
    if n == 1:
        return(n)
    else:
        i = 2
        while i//2 + 1 <= n:
            if n % i == 0:
                if prime(i) == 'none':
                    A = A
                else:
                    A.append(i)
                i += 1
            else:
                i += 1
    n = n - 1
    j = 0
    while n > 0:
        g = 0
        for k in range(len(A)):
             if n % A[k] != 0:
                 g = g
             else:
                 g += 1
        if g == 0:
            j += 1
        n -= 1
    return(j)
with open('text2.txt', 'r') as inf:
    s = inf.readline().strip().split()
    b = []
    for k in range(len(s)):
        b.append(elier_funk(int(s[k])))
res = 1
for i in range(len(b)):
    res *= int(b[i])
print(res**(1/(len(b))))