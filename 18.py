# задача №1
# Напишите программу, которая удаляет из массива
# все простые числа встречающиеся больше одного раза.
n = int(input())
B = []
A = [0 for i in range(n)]
for i in range(n):
    A[i] = int(input())
for i in range(n):
    if A[i] <= 1:
        B.append(A[i])
    else:
        k = 0
        for j in range(2, (A[i] // 2)+1):
            if A[i] % j == 0:
                k = k + 1
            else:
                k = k
        if k >= 1:
            B.append(A[i])
        else:
            h = 0
            for g in range(1, n):
                if A[i] == A[g]:
                    h = h + 1
                else:
                    h = h
            if h >= 2:
                B = B
            else:
                B.append(A[i])
print(B)