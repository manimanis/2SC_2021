from random import randint

# (1) Placer les joueurs en position de départ
pos_lievre = 0
pos_tortue = 0

# (2) Lancer un dé
de = randint(1, 6)
print("Dé =", de)

# (3) Déplacer les joueurs
if de != 6:
    pos_tortue = pos_tortue + 1
    print("La tortue avance à la case", pos_tortue)
else:
    pos_lievre = 6
    print("Le lièvre avance à la position", pos_lievre)