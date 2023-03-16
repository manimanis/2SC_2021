lf1 = 0
while not(lf1 > 0):
    lf1 = int(input("Lessive femme 1 ? "))

lf2 = 0
while not(lf2 > 0):
    lf2 = int(input("Lessive femme 2 ? "))

lf3 = 0
while not(lf3 > 0):
    lf3 = int(input("Lessive femme 3 ? "))

p1 = lf2
while p1 % lf3 != 0:
    p1 = p1 + lf2

p2 = lf1
while p2 % p1 != 0:
    p2 = p2 + lf1

ltf = p2

print(f"Toutes les femmes feront leurs lessives après {ltf} jours")