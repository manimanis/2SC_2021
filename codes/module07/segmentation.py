from random import randint

n = 0
while not (2 <= n <= 20):
    n = int(input("Taille du tableau  ? "))

t = [0]*n
for i in range(n):
    t[i] = randint(1, 999)

print("Avant segmentation : ", t)

j = n
i = 1
while i < j:
    if t[i] > t[0]:
        j -= 1
        t[i], t[j] = t[j], t[i]
    else:
        i += 1
t[j-1], t[0] = t[0], t[j-1]

print("Après segmentation : ", t)

