r1 = float(input("Rayon de C1 ? "))
r2 = float(input("Rayon de C2 ? "))
d = float(input("Distance entre les centres ? "))

if (r1+r2) > d:
    print("Les cercles se coupent en deux points")
elif (r1+r2) < d:
    print("Les cercles ne se coupent pas")
else:
    print("Les deux cercles sont tangentes")
