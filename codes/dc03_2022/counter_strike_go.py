from numpy import array


def saisie_nbj():
    nbj = 0
    while not 3 <= nbj <= 100:
        nbj = int(input("Nombre de joueurs (3 ≤ nbj ≤ 100) ? "))
    return nbj


def remplir_joueurs(nbj):
    joueur = array([str]*nbj)
    for i in range(nbj):
        joueur[i] = ""
        while len(joueur[i]) < 3 or existe(joueur[i], joueur, i):
            joueur[i] = input(f"Joueur n°{i+1} ? ")
    return joueur


def existe(nom, joueur, n):
    tr = False
    i = 0
    while not tr and i < n:
        tr = nom.upper() == joueur[i].upper()
        i += 1
    return tr


def remplir_score(nbj, joueur):
    score = array([int()]*nbj)
    for i in range(nbj):
        score[i] = -1
        while score[i] < 0 or score[i] > 1000:
            score[i] = int(input(f"Score {joueur[i]} ? "))
    return score


def tri_joueurs(nbj, joueur, score):
    for i in range(nbj-1):
        for j in range(i+1, nbj):
            if score[j] > score[i]:
                score[j], score[i] = score[i], score[j]
                joueur[j], joueur[i] = joueur[i], joueur[j]


def aff_scores(nbj, joueur, score):
    rang = 1
    for i in range(nbj):
        if i > 0 and score[i] != score[i-1]:
            rang += 1
        print(rang, "-", joueur[i], f"({score[i]})")


# PP
nbj = saisie_nbj()
joueur = remplir_joueurs(nbj)
score = remplir_score(nbj, joueur)
tri_joueurs(nbj, joueur, score)
aff_scores(nbj, joueur, score)
