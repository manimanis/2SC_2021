from random import randint
from numpy import array
# Programme Pair_Impair
# Saisie de n (5 ≤ n ≤ 15)
n = 0
while not (5 <= n <= 15):
    n= int(input("Nombre de valeurs [5, 15] ? "))
# Déclaration des tableaux
t = array([0]*15)
tp = array([0]*15)
ti = array([0]*15)
# Remplir le tableau t de valeurs aléatoires
for i in range(n):
    t[i] = randint(1, 40)
# Afficher les valeurs du tableau
print("Classer les nombres : pairs/impairs")
for i in range(n):
    print(t[i])
# Classer les valeurs
ni = 0
np = 0
for i in range(n):
    if t[i] % 2 == 0:
        tp[np] = t[i]
        np = np + 1
    else:
        ti[ni] = t[i]
        ni = ni + 1
# Afficher les nombres impairs
print("Liste des nombres impairs")
for i in range(ni):
    print(ti[i])
# Afficher les nombres pairs
print("Liste des nombres pairs")
for i in range(np):
    print(tp[i])
