def saisie():
    n = 0
    while n <= 0:
        n = int(input("Nbre > 0 ? ")) 
    return n


def somme(a, b):
    s = a + b
    return s


# PP
a = saisie()
b = saisie()
c = saisie()
res = somme(a, somme(b, c))
print(a, '+', b, '+', c, '=', res)