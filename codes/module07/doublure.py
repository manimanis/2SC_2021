from random import randint

car = -1
while not (0 <= car <= 100):
    car = int(input("Caractéristique de l'acteur ? "))

n = 0
while not (2 <= n <= 10):
    n = int(input("Nombre de doublures ? "))

t = [0]*n
for i in range(n):
    t[i] = randint(0, 100)

print("Caractéristiques des doublures :", t)

cand = 0
for i in range(n):
    if abs(t[i] - car) < abs(t[cand] - car):
        cand = i

print("Le candidat est n°", cand, "sa caractéristique est", t[cand])