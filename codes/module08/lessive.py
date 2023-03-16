def saisie(msg):
    """Saisir un nombre > 0"""
    nj = 0
    while not(nj > 0):
        nj = int(input(msg))
    return nj


def ppcm(a, b):
    """Calculer le PPCM de deux nombres a et b"""
    p = a
    while p % b != 0:
        p = p + a
    return p


## Programme principal
lf1 = saisie("Lessive femme 1 ? ")
lf2 = saisie("Lessive femme 2 ? ")
lf3 = saisie("Lessive femme 3 ? ")

ltf = ppcm(lf1, ppcm(lf2, lf3))

print(f"Toutes les femmes feront leurs lessives après {ltf} jours")