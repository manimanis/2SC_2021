def saisie(msg):
    n = 0
    while n <= 0:
        n = int(input(msg))
    return n


def som_div(n):
    sn = 0
    for i in range(1, n // 2+1):
        if n % i == 0:
            sn = sn + i
    return sn


# Saisie de deux nombres strictement positifs
n = saisie("Donner n ? ")
m = saisie("Donner m ? ")
# calcul de la somme diviseurs de n
sn = som_div(n)
# calcul de la somme diviseurs de m
sm = som_div(m)
# Affichage du résultat
if (n == sm) and (m == sn):
    print(n, "et", m, "sont amicaux.")
else:
    print(n, "et", m, "ne sont pas amicaux.")