time = input("Affichage du chronomètre ? ")
pdp = time.find(":")

h = int(time[:pdp])
m = int(time[pdp+1:pdp+3])
s = int(time[pdp+4:])

nbs = h * 3600 + m * 60 + s

print(time, "vaut", nbs, "secondes")