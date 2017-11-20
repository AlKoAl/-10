# задача 5
n = input()
while len(n) != 0:
    k = n.count(n[0])
    a = n[0]
    print(n[0], k)
    while k != 0:
        b = n.rfind(a)
        if b > -1:
            n = n[0: b]+n[b+1: len(n)]
        k = k - 1