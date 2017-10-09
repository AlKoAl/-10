# задача 2
# Условие: Напишите программу проверяющую является ли число составным.
# В программе гарантируется, что число - натуральное.
K = int(input())
a = 0
if K == 1:
    print (K,':Unite')
else:
    for i in range(2, K // 2):
        if K % i == 0:
            a = a + 1
        else:
            a = a
    if a >= 1:
        print(K,':Composite')
    else:
        print(K,':Prime')