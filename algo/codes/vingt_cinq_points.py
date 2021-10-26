from random import randint

de1 = randint(1, 6)
de2 = randint(1, 6)
total = de1 + de2

print("Vous avez obtenu", de1, "et", de2)

score = 0
if de1 == de2:
    if de1 == 1 or de1 == 2 or de1 == 4 or de1 == 5:
        score = 5
    elif de1 == 6:
        score = 25

print("Votre score est :", score)
     