primes = [2, 3]
last_crossed = [2, 3]


def add_next_prime():
    candidate = primes[-1] + 2
    i = 0
    while i < len(primes):
        while last_crossed[i] < candidate:
            last_crossed[i] += primes[i]
        if last_crossed[i] == candidate:
            candidate += 2
            i = 0
        i += 1

    primes.append(candidate)
    last_crossed.append(candidate)


def fill_primes(n):
    while len(primes) < n:
        add_next_prime()


n = int(input("Введите номер простого числа: "))
fill_primes(n)
p = primes[n - 1]
print("Первое простое число:", p)
n = int(input("Введите номер простого числа: "))
fill_primes(n)
q = primes[n - 1]
print("Второе простое число:", q)
n = p*q
print("Число n:", n)
euler = (p - 1)*(q - 1)
print("Функция Эйлера:", euler)


def e_and_n():
    global euler, n
    i = 3
    Eratosthenes = [2]
    while i < euler:
        g = 0
        for k in Eratosthenes:
            if i % k == 0:
                g = 1
                break
        if g == 0:
            Eratosthenes.append(i)
        g = 0
        i += 1

    def find_e(x):

        import random
        nonlocal Eratosthenes
        e = (random.choice(Eratosthenes))
        if euler % e != 0:
            return e
        else:
            return find_e(x)
    e = find_e(euler)
    return e


e = e_and_n()
open_key = [e, n]
print("open_key:", open_key)


def d_and_n():
    global e, euler
    d = 1
    while True:
            a = e * d // euler
            if e * d == euler * a + 1:
                if d != e:
                    return d
                else:
                    d += 1
                    continue
            d += 1


d = (d_and_n())
print(d)
closed_key = [d, n]
print("closed_key:", closed_key)
P = int(input("Введите число:"))


def encryption_re(a, b, c):
    d = a % c
    while b > 0:
        d = d % c
        d = d*a
        b = b - 1
    import math
    a = math.fabs(a)
    d = d / a
    return int(d)


coded = encryption_re(P, e, n)
print("Закодированное сообщение:", coded)
recoded = encryption_re(coded, d, n)
print("Раскодированное сообщение:", recoded)
