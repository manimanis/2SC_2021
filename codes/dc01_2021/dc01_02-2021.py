# Partie 1
# Saisie des trois notes de jury
nj1 = int(input("Note du 1er Jury ? "))
nj2 = int(input("Note du 2ème Jury ? "))
nj3 = int(input("Note du 3ème Jury ? "))
# Calcul de la moyenne
m = (nj1 + nj2 + nj3) // 3
# Affichage de la moyenne
print("Abrar et Safa ont obtenu", m, "points")

# Partie 2
# Saisie du nombre de votes nbv
nbv = int(input("Nombre de votes ? "))
# Calcul du bonus
if nbv >= 1000:
    b = 1
else:
    b = 0
# Calcul du score final
score = m + b
print("Le score de Safa et Abrar est de", score, "points")

# Partie 3
# Saisie du temps de l'épreuve te
te = int(input("Temps de l'épreuve ? "))
# Supposer que le temps de retard est nul
tr = 0
if te > 20: # calculer le temps de retard
    tr = te - 20
# Calcul du nombre de points à sanctionner
# un point pour chaque 3 minutes de retard
nps = tr // 3
# Calculer le score final
score = score - nps
# Affichage du score final
print("Temps de retard :", tr, "minutes")
print("Pénalité de retard :", nps, "points")
print("Score final des participantes :", score, "points")