# задача №1
# Напишите программу, которая обрабатывает файл “1-in.txt” с результатами сессии студентов.
# В файле в первой строке лежит число студентов, количество зачетов и экзаменов.
# Затем про каждого студента: ФИО, результаты зачетов(зачтено/незачтено) и оценки за экзамены.
# Программа должна в файл “1-out.txt" записать информацию про каждую категорию  студентов:
# стипендианты(все сдано с оценками не ниже 4),
# отчисленные(более двух предметов не сдано),
# должники(что-то не сдано, но не больше 2-х долгов), остальные.
# Выходной файл должен состоять из 8 строк: 1 строка
# Стипендианты: количество, 2 строка) Фамилии стипендиантов...
f = open('1-in.txt')               # вводымый выводимый файл на английском! т.к. по-другому не работает
g = open('1-out.txt', "w")         # выводимый тоже
k = 0
a = []
w = 0
e = 0
r = 0
t = 0
n1 = []
nk1 = 0
n2 = []
nk2 = 0
n3 = []
nk3 = 0
n4 = []
nk4 = 0
number = 0
passing = 0
exam = 0
for line in f:
    a.append(line)
    k = k + 1
c = a[0].split()
number = int(c[3])
passing = int(c[7])
exam = int(c[11])
for i in range(k-1):
    (len(a[i]))
    a[i] = (a[i][0:(len(a[i])-1)])
for i in range(1, k):
    b = [j for j in a[i].split()]
    for q in range(len(b)):
            if b[q].isdigit():
                if b[q] == '2':
                    w = w + 1
                else:
                    w = w
                if int(b[q]) >= 4:
                    r = r + 1
                else:
                    r = r
            if b[q] == 'not':
                e = e + 1
            else:
                e = e
            if b[q] == 'pass':
                t = t + 1
            else:
                t = t
    if (t == passing) and (r == exam):
        n1.append((b[0])[1] + (b[0])[3])
        nk1 = nk1 + 1
    elif e + w > 2:
        n2.append((b[0])[1] + (b[0])[3])
        nk2 = nk2 + 1
    elif 0 < e + w <= 2:
        n3.append((b[0])[1] + (b[0])[3])
        nk3 = nk3 + 1
    else:
        n4.append((b[0])[1] + (b[0])[3])
        nk4 = nk4 + 1
    e = 0
    w = 0
    r = 0
    t = 0
str1 = ' '.join(n1)
str2 = ' '.join(n2)
str3 = ' '.join(n3)
str4 = ' '.join(n4)
g.write(('number of having scholarships: ' + str(nk1))+'\n')
g.write(('having scholarships: ' + str1)+'\n')
g.write(('number of expelled: ' + str(nk2))+'\n')
g.write(('expelled: ' + str2)+'\n')
g.write(('number of debtors: ' + str(nk3))+'\n')
g.write(('debtors: ' + str3)+'\n')
g.write(('number of others: ' + str(nk4))+'\n')
g.write(('others: ' + str4))
g.close()