U = float(input("Tension d'alimentation ? "))
Uf = float(input("Tension LED ? "))
If = float(input("Courant diode mA ? "))

R = (U - Uf) * 1000 / If

print("R =", int(R), "Ω")