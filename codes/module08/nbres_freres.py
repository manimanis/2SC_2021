def saisie(msg):
    """Saisie d'un nombre strictement positif."""
    n = 0
    while not (n > 0):
        n = int(input(msg))
    return n


def chiff_dist(n):
    """Extraire les chiffres qui composent n dans l'ordre."""
    nch = str(n)
    cd = ""
    for i in range(10):
        c = str(i)
        if c in nch and c not in cd:
            cd = cd + c
    return cd


def freres(n1, n2):
    return chiff_dist(n1) == chiff_dist(n2)


# ----------------------
# Programme Principal
n1 = saisie("Donner n1 > 0 ? ")
n2 = saisie("Donner n2 > 0 ? ")

if freres(n1, n2):
    print(f"{n1} et {n2} sont frères")
else:
    print(f"{n1} et {n2} ne sont pas frères")
