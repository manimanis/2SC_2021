from random import randint
from numpy import array

CAP = 1


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


def saisie_num_etage(ne):
    e = ne
    while e < 0 or e >= ne:
        e = int(input(f"Etage (0 ≤ e < {ne}) ? "))
    return e


def init_parking(ne):
    etages = array([int()]*ne)
    for i in range(ne):
        etages[i] = randint(0, CAP)
    return etages


def calc_nb_places(cp, ne, etages):
    npo = 0
    for i in range(ne):
        npo += etages[i]
    return npo, cp - npo


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


def simuler_entree(p, ne, etages):
    if 0 <= p < ne and etages[p] < CAP:
        etages[p] += 1
        return True
    return False


def simuler_sortie(p, ne, etages):
    if 0 <= p < ne and etages[p] > 0:
        etages[p] -= 1
        return True
    return False


def afficher_parking(cp, ne, etages):
    print()
    print("-" * 40)
    print("Informations parking")
    print("-" * 40)
    print()
    print("Nombre d'étages :", ne)
    print("Capacité :", cp)
    for i in range(ne-1, -1, -1):
        print(f"Etage {i} - {etages[i]} véhicules")
    npo, npv = calc_nb_places(cp, ne, etages)
    print(f"Nombre de places vides : {npv}")
    print(f"Nombre de places occupées : {npo}")
    print()


def entree_parking(ne, etages):
    print()
    print("-" * 40)
    print("Entrée véhicule")
    print("-" * 40)
    pe = chercher_vide(ne, etages)
    if pe == -1:
        return
    e = saisie_num_etage(ne)
    success = simuler_entree(e, ne, etages)
    if success:
        print(f"Entrée véhicule étage {e} accordée.")
    else:
        print(f"Entrée véhicule étage {e} refusée.")


def sortie_parking(ne, etages):
    print()
    print("-" * 40)
    print("Sortie véhicule")
    print("-" * 40)
    print()
    pe = chercher_non_vide(ne, etages)
    if pe == -1:
        return
    e = saisie_num_etage(ne)
    success = simuler_sortie(e, ne, etages)
    if success:
        print(f"Sortie véhicule étage {e} accordée.")
    else:
        print(f"Sortie véhicule étage {e} refusée.")


def chercher_vide(ne, etages):
    e = chercher_place_vide(ne, etages)
    if e != -1:
        print(f"Il y a une place vide dans l'étage {e}.")
    else:
        print("Parking complet!")
    print()
    return e


def chercher_non_vide(ne, etages):
    e = chercher_etage_nonvide(ne, etages)
    if e != -1:
        print(f"Il y a un véhicule dans l'étage {e}.")
    else:
        print("Parking vide!")
    print()
    return e


def menu():
    global ne, etages, cp
    while True:
        print()
        print("-- Menu principal --")
        print()
        print("1- Afficher informations parking")
        print("2- Entrée parking")
        print("3- Sortie parking")
        print("4- Chercher place vide")
        print("5- Chercher place non vide")
        print("X- Quitter")
        rep = input("Votre choix ? ")
        if rep == "1":
            afficher_parking(cp, ne, etages)
        elif rep == "2":
            entree_parking(ne, etages)
        elif rep == "3":
            sortie_parking(ne, etages)
        elif rep == "4":
            chercher_vide(ne, etages)
        elif rep == "5":
            chercher_non_vide(ne, etages)
        elif rep == "6":
            pass
        elif rep == "X" or rep == "x":
            print("Goodbye!")
            break


# PP
ne = saisie_nb_etages()
cp = ne * CAP

etages = init_parking(ne)
afficher_parking(cp, ne, etages)

menu()
