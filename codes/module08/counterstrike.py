from numpy import array


def saisie_nbre_joueurs():
    nh = 0
    while nh < 2 or nh > 8:
        nh = int(input("Nombre de joueurs humains (2 ≤ nh ≤ 8) ? "))
    return nh

def saisie_joueurs(nh):
    ct = array([str]*4)
    te = array([str]*4)
    nct = 0
    nte = 0
    for i in range(nh):
        nj = input(f"Joueur n°{i+1} ? ")
        if nte < 4 and nct < 4:
            eq = 0
            while eq not in [1, 2]:
                eq = int(input("Equipe (1: CT, 2: TE) ? "))
        elif nte == 4:
            eq = 1
        else:
            eq = 2
        if eq == 1:
            ct[nct] = nj
            nct += 1
            neq = "Contre-Terroristes"
        else:
            te[nte] = nj
            nte += 1
            neq = "Terroristes"
        print(f"Equipe : {neq}")
    return te, nte, ct, nct

def ajout_bots(te, nte, ct, nct):
    nb = 1
    for i in range(4):
        if i == nte:
            te[i] = f"Bot-{nb}"
            nte += 1
            nb += 1
        if i == nct:
            ct[i] = f"Bot-{nb}"
            nct += 1
            nb += 1

def afficher_equipes(te, ct):
    print("Equipes".center(60))
    print("Contre-terroristes".center(29) + "|" + "Terroristes".center(29))
    for i in range(4):
        print(f"{i+1}. {ct[i]:<26} | {i+1}. {te[i]:<26}")


nh = saisie_nbre_joueurs()
te, nte, ct, nct = saisie_joueurs(nh)
ajout_bots(te, nte, ct, nct)
afficher_equipes(te, ct)

"""Exemple 1
3
Ahmed
1
Ayhem
2
Raslène
1
"""

"""Exemple 2
6
Adam
2
Malek
1
Amal
1
Lina
1
Fédi
1
Abrar
"""
