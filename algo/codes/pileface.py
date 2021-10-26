from random import randint

choix = int(input("Votre choix (0: Pile/ 1: Face) ? "))
tirage = randint(0, 1)

if choix == tirage:
    print("Vous gagnez!")
else:
    print("Vous perdez!")