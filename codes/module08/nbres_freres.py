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


# ----------------------
# Programme Principal
a = saisie("Donner a > 0 ? ")
b = saisie("Donner b > 0 ? ")

if chiff_dist(a) == chiff_dist(b):
    print(f"{a} et {b} sont frères")
else:
    print(f"{a} et {b} ne sont pas frères")
