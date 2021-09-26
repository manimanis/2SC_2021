etat = input("Etat de l'abreuvoir (V : vide / R : Rempli) ? ")

print("Tâches à réaliser :")
print(" - Nettoyer l'étable")
if etat == 'V' or etat == 'v':
    print(" - Remplir l'abreuvoir")
print(" - Traire les vaches")