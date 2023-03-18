# Saisie de p1 et q1
print("Fraction : p1 / q1")
p1 = int(input("Numérateur ? "))
q1 = 0
while q1 == 0:
    q1 = int(input("Dénominateur ? "))
# Saisie de p2 et q2
p2 = int(input("Numérateur ? "))
q2 = 0
while q2 == 0:
    q2 = int(input("Dénominateur ? "))
# Calcul de la somme des deux fractions
ps = p1 * q2 + p2 * q1
qs = q1 * q2
# Calcul du PGCD(ps, qs)
a = ps
b = qs
while b != 0:
    r = a % b
    a = b
    b = r
# Simplification
ps = ps // a
qs = qs // a
# Affichage
print(p1, "/", q1, "+", p2, "/", q2, "=", ps, "/", qs)