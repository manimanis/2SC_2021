from math import pi

d = float(input("Donner le diamètre de la citerne (m) : "))
h = float(input("Donner l'hauteur de la citerne (m) : "))
nh = int(input("Donner le niveau de l'huile (%) : "))

# volume citerne
vc = pi * d * d * h / 4
# volume de l'huile
vh = int(vc * nh * 10)

print("La citerne contient", vh, "litres d'huile.")
