from random import randint

long = int(input("Longueur du mot de passe ? "))

seq = ""
for i in range(long):
    choix = randint(0, 2)
    if choix == 0:
        seq = seq + chr(65 + randint(0, 25))
    elif choix == 1:
        seq = seq + chr(97 + randint(0, 25))
    else:
        seq = seq + chr(48 + randint(0, 9))
print("Mot de passe :", seq)

nbchiff = 0
nblettmaj = 0
nblettmin = 0
for i in range(len(seq)):
    if "0" <= seq[i] <= "9":
        nbchiff = nbchiff + 1
    elif "A" <= seq[i] <= "Z":
        nblettmaj = nblettmaj + 1
    elif "a" <= seq[i] <= "z":
        nblettmin = nblettmin + 1
print("Nombre de chiffres :", nbchiff)
print("Nombre de lettres majuscules :", nblettmaj)
print("Nombre de lettres minuscules :", nblettmin)

force = (nbchiff + 1) * (nblettmaj + 1) * (nblettmin + 1)
print("Force du mot de passe :", force)
