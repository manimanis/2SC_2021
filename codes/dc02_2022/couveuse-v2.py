from random import randint

no = 0
while no <= 10:
    no = int(input("Nbre d'œufs ? "))

oeufs = "ppppxppppxpppxx"
seq = ""
for i in range(no):
    seq = seq + oeufs[randint(0, len(oeufs) - 1)]
print(seq)

seq1 = ""
for i in range(len(seq)):
    if seq[i] == "p":
        seq1 = seq1 + seq[i]
npv = len(seq1) # Nombre de poussins vifs
print("Nombre de poussins vifs :", npv)

seq2 = ""
nbp = 0
nbc = 0
nbx = 0
for i in range(npv):
    tp = randint(0, 99) # choisir un nombre au hasard entre 0 et 99
    d = tp // 10 # calculer le chiffre de dizaines
    u = tp % 10  # calculer le chiffre des unités
    # Si d = u → le poussin meurt (lettre "x")
    # Si d > u → le poussin devient une poulette (lettre "P")
    # Si d < u → le poussin devient un coquelet (lettre "C")
    if d == u:
        car = "x"
        nbx = nbx + 1
    elif d > u:
        car = "P"
        nbp = nbp + 1
    else:
        car = "C"
        nbc = nbc + 1
    seq2 = seq2 + car
print(seq2)
print("Nombre de poulettes :", nbp)
print("Nombre de coquelets :", nbc)
print("Nombre de poussins morts :", nbx)