def saisie():
    a = 0
    while not (a > 100):
        a = int(input("a > 100 ? "))
    b = a
    while not (a < b < 100000):
        b = int(input(f"{a} < b < 100000 ? "))
    return a, b


def est_prem(n):
    if n < 2:
        return False
    if n == 2:
        return True
    prem = n % 2 != 0
    i = 3
    while prem and i < n // 2:
        prem = n % i != 0
        i = i + 2
    return prem


def est_prem(n):
    nd = 0
    for i in range(1, n+1):
        if n % i == 0:
            nd = nd + 1
    return nd == 2


def est_super(n):
    sup = True
    while sup and n > 0:
        sup = est_prem(n)
        n = n // 10
    return sup


# PP
a, b = saisie()
nsp = 0
for i in range(a, b+1):
    if est_super(i):
        print(i, "est super premier.")
        nsp += 1
print(nsp, f"nombres super premiers dans [{a}, {b}]")