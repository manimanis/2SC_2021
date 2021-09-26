mac = int(input("Montant ? "))
di = input("Devise initiale ($/€/D) ? ")
dr = input("Devise requise ($/€/D) ? ")
if di == '€':
    md = mac
elif di == "$":
    md = mac / 1.17
else:
    md = mac / 3.28

if dr == '€':
    mc = md
elif dr == '$':
    mc = md * 1.17
else:
    mc = md * 3.28

print(mac, di, "=", round(mc, 2), dr)
