n = int(input("Donner un nombre > 0 ? "))

nc = n * n
print(n, "^ 2 =", nc)

nch = str(n)
ncch = str(nc)
print(nch, "est de type", type(nch))
print(ncch, "est de type", type(ncch))

l1 = len(nch)
l2 = len(ncch)
print(n, "contient", l1, "chiffres")
print(nc, "contient", l2, "chiffres")

dcar = ncch[l2-l1:]

automorphe = nch == dcar

print(n, "est automorphe ?", automorphe)