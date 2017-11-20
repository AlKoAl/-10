# задача 3
n = int(input())
a = []
k = 0
c = 0
d = 0
g = 0
b = [n]
for i in range(2, n+1):
    if n % i == 0:
        for j in range(2, (i//2)+1):
            if i % j == 0:
                k = k+1
            else:
                k = k
        if k == 0:
            a.append(i)
k = 0
for i in range(n + 1, n*n + 1):
    for j in range(len(a)):
        if i % a[j] == 0:
            c = c + 1
    if c == 0:
        b.append(i)
        g = i
        for k in range(2, (g // 2) + 1):
            if g % k == 0:
                for j in range(2, (k // 2) + 1):
                    if k % j == 0:
                        d = d + 1
                    else:
                        d = d
                if d == 0:
                    a.append(k)
    c = 0
print(b)