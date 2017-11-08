# задача № 3
# Напишите программу, которая находит во входном потоке простые числа.
# Входной поток заканчивается символом ‘!’.
n = input()
while n != '!':
    if n.isdigit():
        a = int(n)
        k = 0
        if a == 1:
            print(n, ':Unite')
        else:
            for i in range(2, (a // 2)+1):
                if a % i == 0:
                    k = k + 1
                else:
                    k = k
            if k >= 1:
                print(n, ':Composite')
            else:
                print(n, ':Prime')
    else:
        print(n, ':Not a number')
    n = input()