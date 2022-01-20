from random import randint
# (q1)
# seq = ""
# for i in range(10):
#     seq = seq + chr(48 + randint(0, 9))
# print(seq)
# (q2) Le programme génère des séquences de 10 chiffres aléatoires.
# (q3), (q4)
nm = int(input("Donner le nombre de mesures ? "))

seq = ""
for i in range(nm):
    seq = seq + chr(48 + randint(0, 1))
print(seq)

# q(5)
for i in range(randint(1, nm // 5 + (nm % 5 != 0))):
    pos = randint(0, nm-1)
    seq = seq[:pos] + "2" + seq[pos+1:]
print(seq)
# (q6) Le code précédent remplace aléatoirement quelques chiffres de la séquence par le chiffre 2

# (q8)
seq1 = ""
for i in range(nm):
    if seq[i] != "2":
        seq1 = seq1 + seq[i]
seq = seq1
nm = len(seq)
print("Nouvelle séquence :", seq)
print("Longueur de la nouvelle séquence :", nm)

# (q10)
nv = 0
for i in range(nm):
    if seq[i] == "0":
        nv = nv + 1
pv = nv * 100 / nm
print('Nombre de mesures :', nm)
print("Nombre de vibrations :", nv)
print("Pourcentage de vibrations :", round(pv, 2), "%")

# (q12)
if pv >= 60:
    print("Le roulement doit être remplacé")
elif pv >= 50:
    print("Le roulement est usé")
else:
    print("Le roulement en bon état")
