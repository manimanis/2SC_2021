from numpy import array


def saisie():
    n = 4
    while not (5 <= n <= 20):
        n = int(input("Donner la taille du tableau ? "))
    return n


def remplir(n):
    t = array([int()]*n)
    for i in range(n):
        t[i] = -11
        while not ((i == 0 and -10 <= t[i] <= 10) or (i > 0 and t[i] > t[i-1])):
            t[i] = int(input((f"Donner l'élément n°{i} ? ")))
    return t


def position(a, n, t):
    i = -1
    while True:
        i = i + 1
        if (i == n) or (t[i] > a):
            break
    return i


n = saisie()
t = remplir(n)
a = int(input("Donner un entier ? "))
p = position(a, n, t)
print("p =", p)

"""
6
-2
1
5
7
12
26
"""
