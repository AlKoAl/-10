# задача № 2
# Напишите программу, которая подсчитывает,
# сколько раз в строке встретился символ ‘w’.
Ar = [i for i in input().split()]
n = (len(Ar))
s = 0
for j in range(n):
    Str = Ar[j]
    k = len(Str)
    for g in range(k):
        if Str[g] == 'w':
            s = s+1
print(s)