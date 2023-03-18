def saisie_frac(msg):
    print(msg)
    p = int(input("Numérateur ? "))
    q = 0
    while q == 0:
        q = int(input("Dénominateur ? "))
    return p, q


def somme_frac(a1, b1, a2, b2):
    a3 = a1 * b2 + a2 * b1
    b3 = b1 * b2
    return a3, b3


def simp_frac(a, b):
    p = pgcd(a, b)
    a = a // p
    b = b // p
    return a, b


def pgcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# Saisie de p1 et q1 / p2 et q2
p1, q1 = saisie_frac("Fraction : p1 / q1")
p2, q2 = saisie_frac("Fraction : p2 / q2")
# Calcul de la somme des deux fractions
ps, qs = somme_frac(p1, q1, p2, q2)
# Simplification
ps, qs = simp_frac(ps, qs)
# Affichage
print(p1, "/", q1, "+", p2, "/", q2, "=", ps, "/", qs)
