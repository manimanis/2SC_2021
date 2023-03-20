from random import randint
from numpy import array

CAP = 8


def saisie_nb_etages():
    ne = 0
    while ne < 2 or ne > 10:
        ne = int(input("Nombre d'étages du parking (2 ≤ ne ≤ 10) ? "))
    return ne


def saisie_nb_ops():
    no = -1
    while no < 0 or no > 6000:
        no = int(input("Nombre d'opérations (0 ≤ no ≤ 6000) ? "))
    return no


def init_parking(ne):
    etages = array([int()]*ne)
    for i in range(ne):
        etages[i] = randint(0, CAP)
    return etages


def aff_parking(ne, etages):
    for i in range(ne-1, -1, -1):
        print(f"Etage {i} - {etages[i]} véhicules")


def calc_nb_places(cp, ne, etages):
    npo = 0
    for i in range(ne):
        npo += etages[i]
    return npo, cp - npo


def aff_places(npo, npv):
    print(f"Nombre de places vides : {npv}")
    print(f"Nombre de places occupées : {npo}")


def chercher_place_vide(ne, etages):
    p = -1
    i = ne - 1
    while p == -1 and i >= 0:
        if etages[i] < CAP:
            p = i
        else:
            i -= 1
    return p


def chercher_etage_nonvide(ne, etages):
    p = -1
    i = 0
    while p == -1 and i < ne:
        if etages[i] > 0:
            p = i
        else:
            i += 1
    return p


def simuler_entree(ne, etages):
    p = chercher_place_vide(ne, etages)
    if p != -1:
        etages[p] += 1
    return p != -1


def simuler_sortie(ne, etages):
    p = chercher_etage_nonvide(ne, etages)
    if p != -1:
        etages[p] -= 1
    return p != -1


def simuler_entr_sort(no, cp, ne, etages):
    npo, npv = calc_nb_places(cp, ne, etages)
    entree, sortie = 0, 0
    for i in range(no):
        if npv > 0 and npo > 0:
            op = randint(0, 1)
        elif npv == 0:
            op = 1
        elif npo == 0:
            op = 0
        if op == 0:
            simuler_entree(ne, etages)
            entree += 1
            npo += 1
            npv -= 1
        else:
            simuler_sortie(ne, etages)
            sortie += 1
            npo -= 1
            npv += 1
    return npo, npv, entree, sortie


# PP
ne = saisie_nb_etages()
cp = ne * CAP
print("Capacité du parking :", cp)

etages = init_parking(ne)
aff_parking(ne, etages)

npo, npv = calc_nb_places(cp, ne, etages)
aff_places(npo, npv)

no = saisie_nb_ops()
npo, npv, entree, sortie = simuler_entr_sort(no, cp, ne, etages)
print(f"{entree} entrées - {sortie} sorties")

aff_parking(ne, etages)
aff_places(npo, npv)
