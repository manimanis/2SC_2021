print("Vendeur ambulant")
print("==-" * 15)
print("Indiquer le nombre d'articles de chaque catégorie :")
na = int(input("Catégorie A ? "))
nb = int(input("Catégorie B ? "))
nc = int(input("Catégorie C ? "))
ca = na + nb * 3 + nc * 5
print("Le chiffre d'affaires de la journée :", ca, "DT")
if ca >= 150:
    app = "Bon"
elif ca >= 100:
    app = "Satisfaisant"
else:
    app = "Mauvais"
print("Le chiffre d'affaire est", app)