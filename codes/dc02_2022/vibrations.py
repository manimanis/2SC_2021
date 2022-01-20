from random import randint

nm = int(input("Nombre de mesures ? "))

seq = ""
for i in range(nm):
    seq = seq + chr(48 + randint(0, 1))
print(seq)

for i in range(randint(1, nm // 3 + (nm % 3 != 0))):
    pos = randint(0, nm-1)
    seq = seq[:pos] + "2" + seq[pos+1:]
print(seq)

nmi = 0
for i in range(nm):
    if seq[i] == "2":
        nmi = nmi + 1
print("Nombre de mesures incorrectes :", nmi)

for i in range(nm-1, -1, -1):
    if seq[i] == "2":
        seq = seq[:i] + seq[i+1:]
print(seq)
nm = len(seq)

nv = 0
for i in range(nm):
    if seq[i] == "0":
        nv = nv + 1
pv = nv * 100 / nm
print("Nombre de mesures :", nm)
print("Nombre de vibrations :", nv)
print("Pourcentage de vibrations :", round(pv, 2), "%")

if pv >= 60:
    print("Le roulement doit être remplacé")
elif pv >= 50:
    print("Le roulement est usé")
else:
    print("Le roulement est en bon état")


