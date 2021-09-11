d = float(input("Distance en km ? "))
v1 = float(input("Vitesse de Sahbi km/h ? "))
v2 = float(input("Vitesse de Sofien km/h ? "))

t = d / (v1 + v2)
p1 = v1 * t
p2 = v2 * t

ts = int(t * 3600)
tmn = ts // 60
tsc = ts % 60

print("Rencontre après", tmn, "mn et", tsc, "s")
print("Sahbi se trouve à", round(p1, 3), "km de sa maison")
print("Sofien se trouve à", round(p2, 3), "km de sa maison")