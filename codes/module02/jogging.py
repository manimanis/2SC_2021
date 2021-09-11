tj = int(input("Temps jogging (s) ? "))
nbt = int(input("Nombre de tours ? "))

a = int(input("Longueur de la base (m) ? "))
b = int(input("Longueur de l'hauteur (m) ? "))
c = int((a*a+b*b)**0.5)

pq = (a + b + c)
v = pq * nbt / tj

print("Vitesse de Samir =", int(v), "m/s = ", int(v*3.6), "km/h")