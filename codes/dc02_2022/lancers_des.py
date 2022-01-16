from random import randint

npc = randint(1, 6) + randint(1, 6)
print("Lancer PC :", npc)
if npc > 9:
    print("Vous gagnez.")
else:
    nj = int(input("Saisir un nombre entre 0 et 10 ? "))
    no = randint(0, 10)
    nut = (nj + no) % 10 + 2
    print("Lancer joueur :", nut)
    if nut > 9 or nut < npc:
        print("Vous perdez.")
    elif nut > npc:
        print("Vous gagner.")
    else:
        print("Match nul.")
