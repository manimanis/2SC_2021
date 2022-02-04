a = int(input("Donner a ? "))
b = int(input("Donner b ? "))
cpt = 0
for i in range(a, b+1):
    ch = str(i)
    for j in range(len(ch)):
        if ch[j] == '8':
            cpt = cpt + 1
print("Il y a", cpt, "apparition du chiffre 8")