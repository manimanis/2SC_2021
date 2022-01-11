pa = int(input("Numéro de page actuelle ? "))
nbp = 2
nbm = 20
deb = pa - nbp
fin = pa + nbp
if deb < 1:
    deb = 1
if deb + 2*nbp > nbm:
    deb = nbm - 2 * nbp
fin = deb + 2*nbp
for i in range(deb, fin+1):
    if i != pa:
        print(i, end=" ")
    else:
        print(f"[{i}]", end=" ")
print()
