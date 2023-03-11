from random import randint


mot1 = ""
valide = False
while not valide:
    mot1 = input("Mot joueur 1 ? ")
    valide = len(mot1) == 6
    i = 0
    while valide and i < len(mot1):
        valide = 'a' <= mot1[i] <= 'z'
        i += 1

mot2 = ""
while len(mot2) != 6:
    mot2 = input("Mot joueur 2 ? ")
    valide = len(mot2) == 6
    i = 0
    while valide and i < len(mot2):
        valide = 'a' <= mot2[i] <= 'z'
        i += 1

score1, score2 = 0, 0
for i in range(1, 6):
    n = randint(1, 6)
    print(f"Tirage {i} - Dé : {n}")
    if mot1[n-1] > mot2[n-1]:
        print(f"{n}èmes lettres : '{mot1[n-1]}' > '{mot2[n-1]}'")
        score1 += 1
    elif mot1[n-1] < mot2[n-1]:
        print(f"{n}èmes lettres : '{mot1[n-1]}' < '{mot2[n-1]}'")
        score2 += 1
    else:
        print(f"{n}èmes lettres : '{mot1[n-1]}' = '{mot2[n-1]}'")
        if n % 2 == 0:
            print(n, "est pair.")
            score1 += 1
        else:
            print(n, "est impair.")
            score2 += 1
    print("Score 1 =", score1, " - Score 2 =", score2)

if score1 > score2:
    print("Joueur 1 gagne", score1, "contre", score2)
else:
    print("Joueur 2 gagne", score2, "contre", score1)