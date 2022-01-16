hd = int(input("Heure d'arrivée ? "))
hf = int(input("Heure de départ ? "))

if hd <= 3:
    hd = hd + 24
if hf <= 3:
    hf = hf + 24

h10 = hf - hd
h15 = 0
h20 = 0
if hf >= 20:
    if hd < 20:
        h15 = hf - 20
    else:
        h15 = hf - hd
if hf >= 23:
    if hd < 23:
        h20 = hf - 23
    else:
        h20 = hf - hd

pr = h10 * 10 + h15 * 5 + h20 * 5
print("Le montant à payer", pr, "DT")

print("")