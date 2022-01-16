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


