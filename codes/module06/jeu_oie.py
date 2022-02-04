from random import randint

case_finale = 31
pos_j = [0, 0] # utilisateur
num_j = 0
gagne = False
nbre_tours = 0
while not gagne:
    pos_act = pos_j[num_j]
    de1 = randint(1, 6)
    de2 = randint(1, 6)
    s = de1 + de2
    if pos_act + s <= case_finale:
        nouv_pos = pos_act + s
    else:
        nouv_pos = pos_act - s
    print(f"Joueur {num_j+1} obtient {de1}+{de2}={s} : {pos_act} -> {nouv_pos}")
    pos_j[num_j] = nouv_pos
    if pos_j[num_j] == case_finale:
        gagne = True
    else:
        num_j = (num_j + 1) % 2
    nbre_tours += 1
print(nbre_tours)    
