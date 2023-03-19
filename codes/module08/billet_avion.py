def saisie():
    b = ""
    while not valide(b):
        b = input("Numéro de billet ? ")
    return b


def valide(b):
    v = len(b) == 11
    i = 0
    while v and i < len(b):
        v = ("0" <= b[i] <= "9") or ("A" <= b[i] <= "Z")
        i += 1
    return v


def remplacer(b):
    nb = ""
    for i in range(len(b)):
        if "0" <= b[i] <= "9":
            nb += b[i]
        else:
            nb += str(ord(b[i]) - 64)
    return nb


def check_sum(b):
    s = 0
    for i in range(len(b)):
        s += int(b[i])
    return s % 9


# PP
b = saisie()
b1 = remplacer(b)
cs = check_sum(b1)
print("Somme de contrôle :", cs)
if cs == 8:
    print("Billet authentique.")
else:
    print("Billet non authentique.")