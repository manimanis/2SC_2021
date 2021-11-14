# Ex 44
devise1 = input("Devise (E/$) ? ")
montant1 = float(input("Montant de change ? "))

erreur = False
if devise1 == "E":
    devise2 = "$"
    montant2 = montant1 / 0.892
elif devise1 == "$":
    devise2 = "€"
    montant2 = montant1 * 0.892
else:
    erreur = True

if not erreur:
    print(montant1, devise1, "=", round(montant2, 2), devise2)
else:
    print("Je n'ai rien compris")
