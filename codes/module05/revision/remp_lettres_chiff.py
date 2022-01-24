ch = input("Donner une chaine ? ")
remp = "a6e3g9i1o0s5"
ch1 = ""
for i in range(len(ch)):
    if "a" <= ch[i].lower() <= "z":
        pos = remp.find(ch[i])
        if pos != -1:
            ch1 = ch1 + remp[pos+1]
        else:
            ch1 = ch1 + ch[i]
    else:
        ch1 = ch1 + ch[i]
ch = ch1
print(ch)