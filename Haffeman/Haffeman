# кодирование Хаффмана
# программа принимает на вход файл (можете загрузить свой), считывает его, считая количество вхождений
# каждого символа (включая служебные). Кодирует их. Зашифровывает текст в новый файл и добавляет туда словарь
# символ: его бинарный код.
my_file = open('text-in.txt', 'r')    # считал текст из файла
d = {}     # создал пустой словарь. Будущий словарь символ: его количество в тексте
for line in my_file:
    for i in line:
        if i in d.keys():      # Если символ есть в словаре - прибавляем к значению единицу, если нет - записываем его.
            d[i] += 1
        else:
            d[i] = 1
s = {}   # словарь для символ: код
a = {}   # словарь для узлов (Допустим были символы а и б, здесь будет лежать аб = {а: частота, б: частота}
def func_keys_min(x):
    global s
    keys1 = []
    for key in x.keys():
        keys1.append(key)
    if keys1[0] in a:
        keys2 = []
        for key in a[keys1[0]].keys():
            keys2.append(key)  # нашёл ключи ключа полученного словаря
        if len(keys2[0]) >= len(keys2[1]):  # сравниваю значения ключей
            func_keys_max({keys2[0]: (x[keys1[0]] + '1')})
            func_keys_min({keys2[1]: (x[keys1[0]] + '0')})
        else:
            func_keys_max({keys2[1]: (x[keys1[0]] + '1')})
            func_keys_min({keys2[0]: (x[keys1[0]] + '0')})
    else:
        s.update(x)
def func_keys_max(x):
    global s
    keys1 = []
    for key in x.keys():
        keys1.append(key)
    if keys1[0] in a:
        keys2 = []
        for key in a[keys1[0]].keys():
            keys2.append(key)  # нашёл ключи ключа полученного словаря
        if len(keys2[0]) >= len(keys2[1]):  # сравниваю значения ключей
            func_keys_max({keys2[0]: (x[keys1[0]] + '1')})
            func_keys_min({keys2[1]: (x[keys1[0]] + '0')})
        else:
            func_keys_max({keys2[1]: (x[keys1[0]] + '1')})
            func_keys_min({keys2[0]: (x[keys1[0]] + '0')})
    else:
        s.update(x)
def func(x):
    global a  # для изменения а
    l = {}
    massif = []
    for value in x.values():
        massif.append(value)
    massif.sort()        # сортируем значения по возрастанию
    if len(massif) != 1:  #
        x1 = massif[0]
        x2 = massif[1]      # берём два наименьших значения
        for key in x.keys():
            if x1 == x[key]:
                key1 = str(key)
                del x[key]
                break
        for key in x.keys():
            if x2 == x[key]:
                key2 = str(key)     # находим ключи к значениям
                del x[key]          # здесь изначальный словарь уже без двух наименьших элементов
                break
        x[(key1 + key2)] = (x1 + x2)   # добавляем новое значение (аб созданное из а и б)
        l[(key1 + key2)] = {key1: x1, key2: x2}
        a.update(l)   # собственно создаём узел
        func(x)    # работаем с новым списком
func(d)
new_key = ''
for key in a.keys():
    if len(key) > len(new_key):              # нашёл самый длинный узел(корень)
        new_key = key
keys = []
for key in a[new_key].keys():
    keys.append(key)
if len(keys[0]) >= len(keys[1]):
    func_keys_max({keys[0]: '1'})
    func_keys_min({keys[1]: '0'})
else:
    func_keys_max({keys[1]: '1'})
    func_keys_min({keys[0]: '0'})
my_file = open('text-in.txt')
my_out_file = open('text-out.txt', 'w')
for line in my_file:
    for i in line:
        for key in s.keys():
            if i == key:
                my_out_file.write(str(s[key]))
                break
my_out_file = open('text-out.txt', 'a')
my_out_file.write('\n')
my_out_file.write(str(s))
