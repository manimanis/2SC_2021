# Todo 1 : Saisir la valeur des résistances
r1 = float(input("Donner la valeur de R1 ? "))
r2 = float(input("Donner la valeur de R2 ? "))

# Todo 2 : Calculer la résistance équivalente
req = r1 * r2 / (r1 + r2)

print("R1 =", r1, "Ω")
print("R2 =", r2, "Ω")

# Todo 3 : Afficher Req avec seulement 2 décimales
print("Req =", req, "Ω")