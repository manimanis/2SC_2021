from random import randint
nbq = int(input("Nombre de questions ? "))
score = 0
for i in range(nbq):
    v1 = randint(1, 9)
    v2 = randint(1, 9)
    res = v1 * v2
    rep = int(input(f"Question {i+1} / {nbq} : {v1} × {v2} = ? "))
    if rep == res:
        print("Correct!")
        score += 1
    else:
        print(f"Non, {v1} × {v2} = {res}")
print(f"Score : {score} / {nbq}")