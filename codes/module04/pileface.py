from random import randint

print("Choix de l'utilisateur")
ch1 = int(input("0 : Pile / 1 : Face"))

ch2 = randint(0, 1)

if ch1 == ch2:
    print("Vous avez gagné")
else:
    print("Vous avez perdu")
