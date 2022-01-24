ch = input("Donner une chaine ? ")
nc = 0
for i in range(len(ch)):
    if "0" <= ch[i] <= "9":
        nc = nc + 1
print(ch, "contient", nc, "chiffres")
