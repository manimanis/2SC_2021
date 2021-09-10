# Longueur de la pièce en m
long = float(input("Longueur de la pièce en m ? "))
# Largeur de la pièce en m
larg = float(input("Largeur de la pièce en m ? "))
# Nombre de couches de peinture
nbc = int(input("Nombre de couches de peinture ? "))
# Rendement en m²/Kg
rend = float(input("Rendement en m²/Kg ? "))

# Surface du toit m²
st = long * larg
# Surface à peindre
sp = st * nbc
# Quantité de peinture
qp = sp / rend

print("Surface pièce =", st, "m²")
print("Nombre de couches =", nbc)
print("Surface totale =", sp, "m²")
print("Rendement =", rend, "m²/Kg")
print("La quantité de peinture =", qp, "Kg")