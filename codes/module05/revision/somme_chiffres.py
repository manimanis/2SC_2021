ch = input("Donner une chaine ? ")
s = 0
for i in range(len(ch)):
    if "0" <= ch[i] <= "9":
        s = s + int(ch[i])
print("Somme des chiffres de", ch, "est", s)
