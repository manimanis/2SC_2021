from random import randint

nm = 0
while not (10 <= nm <= 1000):
    nm = int(input("Nombre de mesures ? "))

seq = ""
for i in range(nm):
    seq = seq + chr(48 + randint(0, 9))
print("Séq. brute :", seq)

seq1 = ""
nvi, nvt = 0, 0
for i in range(nm):
    # Remplacer les chiffres de la séquence seq par les lettres "n", "i" et "t"
    if seq[i] <= "4":
        seq1 += "n"
    elif seq[i] <= "7":
        seq1 += "i"
        nvi += 1
    else:
        seq1 += "t"
        nvt += 1
print("Vibrations :", seq1)
print("Vibrations importantes :", nvi, "/", nm)
print("Vibr. très importantes :", nvt, "/", nm)

pvi = nvi * 100 // nm
pvt = nvt * 100 // nm
print("Vibrations imp. :", pvi, "%")
print("Vibr. très imp. :", pvt, "%")

seq2 = ""
for i in range(nm):
    if seq1[i] == 't':
        seq2 += 'n'
    else:
        seq2 += seq1[i]
nr = nvt // 10
if nr % 10 != 0:
    nr += 1
print("Nombre de roulements :", nr)
print("Vibrations :", seq2)
        
    
