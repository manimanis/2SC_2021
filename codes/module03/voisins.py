a = int(input("Donner a ? "))
b = int(input("Donner b ? "))

sa = str(a)
sb = str(b)

voisins = sa[-1] == sb[0]

print(a, "et", b, "sont voisins ?", voisins)