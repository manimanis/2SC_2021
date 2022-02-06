from random import randint

case_finale = 32
pos_j = 0
gagne = False
nbre_tours = 0

nbre_tours = nbre_tours + 1
de = randint(1, 6)

nouv_pos = pos_j + de
action = "Av"

print(f"Tour {nbre_tours:2} - Dé : {de} - {action} {pos_j:2} → {nouv_pos:2}")
pos_j = nouv_pos
gagne = pos_j == case_finale

