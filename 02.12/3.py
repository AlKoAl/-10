def Qs(a):
    n = len(a)
    more = []
    equal = []
    less = []
    if len(a) > 1:
        base = a[0]
        for i in range(n):
            if base > a[i]:
                less.append(a[i])
            elif base == a[i]:
                equal.append(a[i])
            else:
                more.append(a[i])
        return Qs(less) + equal + Qs(more)
    else:
        return(a)
a = [int(i) for i in input().split()] # вводите строку с пробелами
print(Qs(a))