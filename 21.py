# задача №2
# Напишите программу, которая обрабатывает результаты IQ-теста из файла “2-in.txt".
# В файле лежат несколько строк со значениями(не менее 4-х).
# Программа должна вывести в консоль среднее арифметическое
# по лучшим трем в каждой строке результатам(одно число).
f = open('2-in.txt')
a = []
b = []
c = []
h = 0
k = 0
d = 0
res = 0
q = 0
for line in f:
    a.append(line)
    k = k + 1
for i in range(k-1):
    (len(a[i]))
    a[i] = (a[i][0:(len(a[i])-1)])
for i in range(1, k):
    b = [j for j in a[i].split()]
    for g in range(len(b)):
        if b[g].isdigit():
            c.append(int(b[g]))
            c.sort()
    for k in range(len(c)):
        if len(c) > 2:
            q = c[len(c) - 1] + c[len(c) - 2] + c[len(c) - 3]
    d = d + 3
    print(q)
    res = res + q
    c = []
    print(d)
print(res/d)