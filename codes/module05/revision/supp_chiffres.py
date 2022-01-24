ch = input("Donner une chaine ? ")
ch1 = ""
for i in range(len(ch)):
    if not ("0" <= ch[i] <= "9"):
        ch1 = ch1 + ch[i]
ch = ch1
print(ch)