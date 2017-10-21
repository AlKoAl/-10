a = []
b = []
h = 2
n = int(input())
d = 0
if n >= 1:
    a.append(2)
    b.append(2)
    d = d + 1
    n = n - 1
    h = h + 1
    while n != 0:
        k = 0
        for i in range(d):
            c = h % b[i]
            if c == 0:
                k = k + 1
        if k == 0:
            b.append(h)
            a.append(h)
            d = d + 1
            n = n - 1
            h = h + 1
        else:
            h = h + 1
print(a)
