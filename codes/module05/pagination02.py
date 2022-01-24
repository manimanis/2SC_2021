nbp = int(input("Nombre de pages ? "))
np = int(input("Page actuelle ? "))
npa = int(input("Nombre de pages affichées ? "))

# 3 pages au minimum
npa = (npa >= 3) * npa + (npa < 3) * 3
# Le nombre de pages ne doit pas être inférieur
# à npa (nombre de pages affichées)
nbp = (nbp >= npa) * nbp + (nbp < npa) * npa

if np < 1: 
    np = 1
elif np > nbp:
    np = nbp

mnpa = npa // 2
if 1 + mnpa <= np <= 20 - mnpa:
    deb = np - mnpa
    fin = deb + npa - 1
elif np <= 1 + mnpa:
    deb = 1
    fin = deb + npa - 1
else:
    fin = nbp
    deb = fin - npa + 1

for i in range(deb, fin+1):
    if i == np:
        print("["+str(i)+"]", end=" ")
    else:
        print(i, end=" ")
print()