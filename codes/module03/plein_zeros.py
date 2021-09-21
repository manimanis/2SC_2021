n = int(input("Donner un nombre de 2 chiffres ? "))

d = n // 10
u = n % 10
n1 = d * 10**(abs(d-u)+1) + u

print(n, "devient", n1)