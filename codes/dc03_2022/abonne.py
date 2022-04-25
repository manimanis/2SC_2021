nbj = 0
while not (3 <= nbj <= 100):
    nbj = int(input("Nombre de joueurs ? "))

joueur = [""]*nbj
for i in range(nbj):
    valide = False
    while not valide:
        joueur[i] = input(f"Joueur n°{i+1} ? ")

        valide = len(joueur[i]) >= 3
        j = i-1
        while valide and j >= 0:
            valide = joueur[j].upper() == joueur[i].upper()
            j = j - 1
        
        if valide:
            print(f"{joueur[i]} existe déjà ou invalide !")


scores = [0]*nbj
for i in range(nbj):
    scores[i] = -1
    while not 0 <= scores[i] <= 1000:
        scores[i] = int(input(f"Score de {joueur[i]} ? "))

for i in range(nbj-1):
    for j in range(nbj-i-1):
        if scores[j] < scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]
            joueur[j], joueur[j+1] = joueur[j+1], joueur[j]

print("Top 3 Scores")
for i in range(3):
    print(f"{joueur[i]:25} - {scores[i]:3}")

"""
10
Ahmed
Yassine
Ayhem
Raed
Kenza
Abrar
Zaineb
Adem
Amel
Malek
37
90
29
38
90
81
72
19
51
8
"""