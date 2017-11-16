# задача №3
# Напишите программу, которая обрабатывает файлы с результатами секвенирования.
# В первой строке файла лежит количество цепочек и другая вспомогательная информация.
# В остальных строчках - последовательности нуклеотидов.
# Если файл корректный - нужно вывести в консоль информацию о том,
# что секвенировалось(DNA/RNA) и информацию  количестве нуклеотидов каждого типа.
# А если файл отсутствует или некорректный - информацию что не так.
f = open('3-in.txt')
a = []
q = 0
w = 0
e = 0
r = 0
t = 0
y = 0
k = 0
for line in f:
    a.append(line)
    k = k + 1
for i in range(k-1):
    (len(a[i]))
    a[i] = (a[i][0:(len(a[i])-1)])
for i in range(1, k):
    for g in range(len(a[i])):
        if ((a[i])[g]).upper() == 'A':
            q = q + 1
        elif ((a[i])[g]).upper() == 'C':
            w = w + 1
        elif ((a[i])[g]).upper() == 'G':
            e = e + 1
        elif ((a[i])[g]).upper() == 'T':
            r = r + 1
        elif ((a[i])[g]).upper() == 'U':
            t = t + 1
        else:
            y = y + 1
if y > 0:
    print('someone is wrong')
elif t > 0 and r > 0:
    print('someone is wrong')
else:
    if t > 0:
         print('RNA')
         print('A:', q)
         print('C:', w)
         print('G:', e)
         print('U:', t)
    else:
         print('DNA')
         print('A:', q)
         print('C:', w)
         print('G:', e)
         print('T:', r)