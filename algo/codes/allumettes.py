n = 1
while not (15 <= n <= 35 and n % 2 == 1):
    n = int(input("Nombre d'allumettes [15, 35] ? "))

jo = ["", ""]
for i in range(2):
    while not jo[i] != "":
        jo[i] = input(f"Pseudo joueur {i+1} ? ")

gagne = -1
nj = 0
nma = 3
while gagne == -1:
    print(f"({nj+1}) {jo[nj]} joue")
    nba = 0
    if nma > n: nma = n
    while not (1 <= nba <= nma):
        nba = int(input(f"Nbre d'alumettes [1, {nma}] ? "))
    n = n - nba
    print("Nombre d'allumettes restantes :", n)
    nj = (nj + 1) % 2
    if n == 0:
        gagne = nj

print(jo[gagne], "gagne la partie.")
