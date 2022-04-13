n = 0
while not (5 <= n <= 20):
    n = int(input("Nbre d'éléments ? "))

t = [0]*n
for i in range(n):
    t[i] = int(input(f"t[{i}] ? "))

sym = True
i = 0
j = n-1
while sym and j > i:
    sym = t[j] == t[i]
    if sym:
        i = i + 1
        j = j - 1

if sym:
    print("Le tableau est symétrique")
else:
    print("Le tableau n'est pas symétrique")

if not sym:
    i1 = i+1
    j1 = j
    sym = True
    while sym and j1 > i1:
        sym = t[j1] == t[i1]
        if sym:
            i1 = i1 + 1
            j1 = j1 - 1

if not sym:
    i1 = i
    j1 = j - 1
    sym = True
    while sym and j1 > i1:
        sym = t[j1] == t[i1]
        if sym:
            i1 = i1 + 1
            j1 = j1 - 1

if sym:
    print("Le tableau peut devenir symétrique")
else:
    print("Le tableau ne peut pas devenir symétrique")

