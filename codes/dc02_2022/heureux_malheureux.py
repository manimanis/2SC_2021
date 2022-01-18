from random import randint

seq = ""
for i in range(8):
    seq = seq + chr(48 + randint(0, 9))
print(seq)

for i in range(2):
    pos = randint(4*i, 4*i+3)
    seq = seq[:pos] + "?" + seq[pos+1:]
print(seq)

pg = 0
for i in range(4):
    if seq[i] != '?':
        pg = pg + int(seq[i])
print("Somme('" + seq[:4]+"') =", pg)

pd = 0
for i in range(4):
    if seq[4+i] != '?':
        pd = pd + int(seq[4+i])
print("Somme('" + seq[4:]+"') =", pd)

mx = (pg >= pd) * pg + (pg < pd) * pd
if pg == mx:
    man1 = "0"
    man2 = str(mx - pd)
else:
    man2 = "0"
    man1 = str(mx - pg)
print("Les chiffres manquants sont :", man1, "et", man2)

heureux = seq
pos = heureux.find('?')
heureux = seq[:pos] + man1 + seq[pos+1:]
pos = heureux.find('?')
heureux = heureux[:pos] + man1 + heureux[pos+1:]

print("Le nombre heureux est : ", heureux)
