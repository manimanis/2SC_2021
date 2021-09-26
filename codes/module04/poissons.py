print("Calcul du prix de vente")
print("==-" * 15)
np = input("Quel est le nom du produit ? ")
pa = float(input("Quel est le prix d'achat (DT) ? "))
if pa < 15:
    gain = 20
elif pa < 30:
    gain = 25
else:
    gain = 35
print("Gain :", gain, "%")
pv = pa * (1 + gain/100)
print("Prix de vente :", round(pv, 3), "DT")