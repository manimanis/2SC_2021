from random import randint

objets = ["Pierre", "Feuille", "Ciseaux"]

print("Jeu Pierre - Feuille - Ciseaux")
print()

j1 = int(input("Votre choix\n0: Pierre/1: Feuille/2: Ciseaux ? "))
j2 = randint(0, 2)

print(objets[j1], "contre", objets[j2])

g = (j1 - j2) % 3

if g == 0:
    print("Match nul")
elif g == 1:
    print("Bravo, vous gagnez!")
else:
    print("Désolé, vous perdez!")