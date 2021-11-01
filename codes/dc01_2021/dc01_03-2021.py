# Partie 1
# Saisie du nombre de parties
npr = int(input("Nombre de parties gagnées par Raed ? "))
npa = int(input("Nombre de parties gagnées par Amir ? "))
npn = int(input("Nombre de parties nulles ? "))
# Calcul du nombre de parties jouées
npj = npr + npa + npn
# Afficher le nombre de parties gagnées
print("Nombre de parties jouées", npj)
print("Raed a gagné", npr, "/", npj, "fois")
print("Amir a gagné", npa, "/", npj, "fois")

# Partie 2
# Affichage du gagnant
if npa == npr:  # match nul
    print("Match null")
else:  # il y a un gagnant
    if npr > npa:  # Raed est le gagnant
        gagnant = "Raed"
        perdant = "Amir"
    elif npr < npa:  # Amir est le gagnant
        gagnant = "Amir"
        perdant = "Raed"
    # afficher le nom du gagnant
    print(gagnant, "gagne contre", perdant)

# Partie 3
# Saisie des numéros des gagnants
ng1 = int(input("Gagnant 1 (0: Raed/ 1: Amir) ? "))
ng2 = int(input("Gagnant 2 (0: Saïd/ 1: Raslène) ? "))
# Calcul des noms des gagnants
if ng1 == 0:  # Raed est gagnant
    g1 = "Raed"
else:  # Amir est gagnant
    g1 = "Amir"
if ng2 == 0:  # Saïd est gagnant
    g2 = "Saïd"
else:  # Raslène est gagnant
    g2 = "Raslène"
# Afficher les noms des finalistes
print("La partie finale se joue entre", g1, "et", g2)
