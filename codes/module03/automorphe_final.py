n = int(input("Donner un nombre > 0 ? "))

nc = n * n
print(n, "^ 2 =", nc)

nch = str(n)
ncch = str(nc)

l = len(nch)

dcar = ncch[-l:]

automorphe = nch = dcar

print(n, "est automorphe ?", automorphe)