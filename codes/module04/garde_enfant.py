hd = int(input("Heure d'arrivée ? "))
hf = int(input("Heure de départ ? "))

if hd <= 3:
    hd = hd + 24
if hf <= 3:
    hf = hf + 24

hg1 = hd - 18
if hg1 <= 2:
    prd = hg1 * 10
elif hg1 <= 5:
    prd = 2 * 10 + (hg1 - 2) * 15
else:
    prd = 2 * 10 + 3 * 15 + (hg1 - 5) * 20

hg2 = hf - 18
if hg2 <= 2:
    prf = hg2 * 10
elif hg2 <= 5:
    prf = 2 * 10 + (hg2 - 2) * 15
else:
    prf = 2 * 10 + 3 * 15 + (hg2 - 5) * 20

pr = prf - prd

print("Le montant à payer", pr, "DT")

print("")