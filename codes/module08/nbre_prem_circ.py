def saisie(msg):
    """Saisie d'un nombre strictement positif."""
    n = 0
    while not (n > 100):
        n = int(input(msg))
    return n


def est_prem(n):
    """Retourne True si n est un nombre premier."""
    if n < 2:
        return False
    if n == 2:
        return True
    prem = n % 2 != 0
    i = 3
    while prem and i < n // 2:
        prem = n % i != 0
        i = i + 2
    return prem


def rotation(ch):
    """Effectue une rotation des chiffres de ch."""
    return ch[1:] + ch[0]


def est_circ(n):
    """Retourne True si n est un nombre premier circulaire."""
    nch = str(n)
    circ = est_prem(n)
    nch1 = rotation(nch)
    while circ and nch1 != nch:
        circ = est_prem(int(nch1))
        nch1 = rotation(nch1)
    return circ


# Programme principal
a = saisie("Donner a > 100 ? ")
if est_circ(a):
    print(f"{a} est un nombre premier circulaire.")
else:
    print(f"{a} n'est pas un nombre premier circulaire.")