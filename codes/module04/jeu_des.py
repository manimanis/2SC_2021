from random import randint
d1 = randint(1, 6)
d2 = randint(1, 6)
d3 = randint(1, 6)
s = d1 + d2 + d3
print('Dé1 :', d1, "- Dé2 :", d2, "- Dé3 :", d3)
print("Somme :", s)
if d1 == d2 == d3:
    print("Vous gagnez 300 pts")
elif d1 == d2 or d2 == d3 or s == 6:
    print("Vous gagnez 200 pts")
elif d1 == 6 or d2 == 6 or d3 == 6:
    print("Vous gagnez 50 pts")
else:
    print("Vous gagnez", s, "pts")