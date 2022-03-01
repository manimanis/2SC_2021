from random import randint


nb = 0
while not 10 <= nb <= 200:
    nb = int(input("Nombre de bonbons [10, 200] ? "))

na = 0
while not 3 <= na <= 10:
    na = int(input("Nombre d'amis [3, 10] ? "))

boite = [0]*na
for i in range(nb):
    nbh = randint(0, na-1)
    boite[nbh] = boite[nbh] + 1

for i in range(na):
    print(f"Boîte {i} contient {boite[i]} bonbons.")