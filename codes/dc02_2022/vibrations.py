from random import randint

seq = ""
for i in range(randint(6, 20)):
    seq = seq + chr(48 + randint(0, 1))
print(seq)

tm = len(seq)
nv = 0
for i in range(tm):
    if seq[i] == "0":
        nv = nv + 1
pv = nv * 100 / tm
print("Taille du message :", tm)
print("Nombre de vibrations :", nv)
print("Pourcentage de vibrations :", round(pv, 2), "%")

if pv >= 65:
    print("Le roulement doit être remplacé")
elif pv >= 55:
    print("Le roulement est usé")
else:
    print("Le roulement est en bon état")


