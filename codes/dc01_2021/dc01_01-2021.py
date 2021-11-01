# Partie 1
# Saisie du nombre d'exercices
ex1 = int(input("Nombre d'exercices Nour ? "))
ex2 = int(input("Nombre d'exercices Amine ? "))
# Calcul de la récompense
rec = (ex2 - ex1) * 5
# Affichage du résultat
print("Amine va jouer", rec, "minutes plus que Nour")

# Partie 2
# Saisie du temps réservé au jeu tj
tj = int(input("Temps réservé au jeu ? "))
# Calcul du temps du jeu de chacun des deux
if rec >= 0:
    tj1 = tj
    tj2 = tj + rec
else:
    tj1 = tj - rec
    tj2 = tj
# Afficher le temps de jeu
print("Nour joue", tj1, "minutes")
print("Amine joue", tj2, "minutes")

# Partie 3
# Saisie du nombre de triches de chacun des jumeaux : n1 et n2
n1 = int(input("Nombre de triches Nour ? "))
n2 = int(input("Nombre de triches Amine ? "))
# Calcul du temps de pénalité
tp1 = 2 * n1
tp2 = 2 * n2
# Afficher le temps de pénalité
print("Nour est pénalisé de", tp1, "minutes")
print("Amine est pénalisé de", tp2, "minutes")