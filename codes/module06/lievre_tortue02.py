from random import randint

# (1) Placer les joueurs en position de départ
pos_lievre = 0
pos_tortue = 0

while pos_lievre != 6 and pos_tortue != 6:
    # (2) Lancer un dé
    de = randint(1, 6)
    print("Dé =", de)

    # (3) Déplacer les joueurs
    if de != 6:
        pos_tortue = pos_tortue + 1
        print("La tortue avance à la case", pos_tortue)
    else:
        pos_lievre = 6
        print("Le lièvre avance à la case", pos_lievre)

print("Le lièvre est en poition", pos_lievre)
print("La tortue est en poition", pos_tortue)

if pos_lievre == 6:
    print("Le lièvre a gagné.")
else:
    print("La tortue a gagné.")