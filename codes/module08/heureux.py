def saisie():
    n = 0
    while (not 2 <= n <= 5):
        n = int(input("Nombre de chiffres ? "))
    return n


def somme_chiff(n):
    s = 0
    while n != 0:
        r = n % 10
        s = s + r*r
        n = n // 10
    return s
 

def est_heureux(n):
    sc = somme_chiff(n)
    while sc >= 10:
        sc = somme_chiff(sc)
    return sc == 9


def intervalle(n):
    deb = 10**(n-1)
    fin = deb * 10 - 1
    return deb, fin


# PP
p = saisie()
deb, fin = intervalle(p)
count = 0
for i in range(deb, fin+1):
    if est_heureux(i):
        print(i, "est heureux.")
        count += 1
print(count, f"nombres heureux dans l'intervalle [{deb}, {fin}].")