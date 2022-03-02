from random import randint
# Saisie du nombre de prix
while not 1 <= np <= 10:
    np = int(input("Donner le nombre de prix (1 ≤ np ≤ 10) ? "))
# Déclaration du tableau des prix
prix = [""] * np
# Saisie des prix
for i in range(np):
    prix[i] = input(f"Donner le nom du {i+1}ème prix ? ")
# Saisie du nombre de participants
while not np <= n <= 20:
    n = int(input(f"Donner le nombre de participants ({np} ≤ n ≤ 20) ? "))
# Déclaration du tableau de participants
noms = [""] * n
# Saisie des noms des participants
for i in range(n):
    noms[i] = input(f"Donner le nom du {i+1}ème participant ? ")
# Tirage au sort
for i in range(n):
    j = randint(0, n-1)
    noms[i], noms[j] = noms[j], noms[i]
# Affichage des gagnants
for i in range(np):
    print(noms[i], "gagne", prix[i])