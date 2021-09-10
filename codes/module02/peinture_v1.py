# Longueur de la pièce en m
long = 6.30 
# Largeur de la pièce en m
larg = 5.20
# Nombre de couches de peinture
nbc = 3
# Rendement en m²/Kg
rend = 6

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