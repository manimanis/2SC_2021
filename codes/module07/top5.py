from random import randint

scores = [0]*6

np = 0
while not 1 <= np <= 50:
    np = int(input("Nombre de parties jouées [1, 50] ? "))

nc = 0
for i in range(np):
    sc = randint(0, 99) * 10
    print(f"Partie {i+1} - score : {sc}")
    
    j = nc-1
    while j >= 0 and scores[j] < sc:
        scores[j+1] = scores[j]
        j -= 1
    scores[j+1] = sc

    if nc < 5:
        nc += 1

pos = ["st", "nd", "rd", "th"]
for i in range(nc):
    if i < 3:
        position = pos[i]
    else:
        position = pos[3]
    print(f"{i+1}{position} {scores[i]}")
    
