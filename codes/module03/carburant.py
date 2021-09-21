print("Le matin")
nd = int(input("Niveau de carburant ? "))
dd = int(input("Nombre de km parcourus ? "))
print("Le soir")
nf = int(input("Niveau de carburant ? "))
df = int(input("Nombre de km parcourus ? "))

cons = nd - nf
dist = df - dd
taux = cons / dist * 100

print("La voiture a consommé", cons, "litres pour", dist, "km")
print("La voiture a consommé", round(taux, 1), "l/100km")