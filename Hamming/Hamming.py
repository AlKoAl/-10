string = input('Введите строку из 0 и 1')
k = 0
while True:
    if k <= 2**k - len(string) - 1:
        break
    else:
        k += 1
string = ' ' + string[:]
for i in range(1, k):
    string = string[: (2 ** i) - 1] + ' ' + string[(2 ** i) - 1:]


def part_of_coding(digits):
    def func1(s):
        nonlocal score, digits
        while s * 2 ** i <= len(digits):
            if s == 1:
                if (s + 1) * 2 ** i > len(digits):
                    for j in digits[s * 2 ** i:]:
                        score += int(j)
                    break
                else:
                    for j in digits[s * 2 ** i: (s + 1) * 2 ** i - 1]:
                        score += int(j)
                    s += 2
                    func1(s)
                    return ()
            else:
                if (s + 1) * 2 ** i > len(digits):
                    for j in digits[s * 2 ** i - 1:]:
                        score += int(j)
                    break
                else:
                    for j in digits[s * 2 ** i - 1: (s + 1) * 2 ** i - 1]:
                        score += int(j)
                    s += 2
                    func1(s)
                    return ()

    for i in range((k - 1), -1, -1):
        score = 0
        func1(1)
        if score % 2 == 0:
            digits = digits[:2 ** i - 1] + '0' + digits[2 ** i:]
        else:
            digits = digits[:2 ** i - 1] + '1' + digits[2 ** i:]
    return(digits)


string = part_of_coding(string)
print("Закодированная последовательность:", string)
error = input("Введите изменённую последовательность с одной ошибкой:")
error = error[2:]
for i in range(k - 1, 1, -1):
    error = error[:(2**i - 3)] + error[(2**i - 2):]
while True:
    if k <= 2**k - len(error) - 1:
        break
    else:
        k += 1
error = ' ' + error[:]
for i in range(1, k):
    error = error[: (2 ** i) - 1] + ' ' + error[(2 ** i) - 1:]
error = part_of_coding(error)
print("Переприсвоение кодирующих бит:", error)
i = 0
numbers = []
while 2**i <= len(string):
    if error[2**i-1] == string[2**i-1]:
        numbers.append(0)
        i += 1
    else:
        numbers.append(1)
        i += 1
sum = 0
for i in range(len(numbers)):
    sum += 2**i*numbers[i]
    print(sum)
print("Ошибочный бит:", sum)
if sum == 0:
    error = error
else:
    if error[sum - 1] == '1':
        error = error[: sum - 1] + '0' + error[sum:]
    elif error[sum - 1] == '0':
        error = error[: sum - 1] + '1' + error[sum:]
error = error[2:]
for i in (1, k + 1):
    error = error[:2**i - 1] + error[2**i:]
print(error)
