from numpy import array

# séquence 1
n = 4
while not (5 <= n <= 20):
    n = int(input("Donner la taille du tableau ? "))

t = array([int()]*n)

# séquence 2
for i in range(n):
    t[i] = -11
    while not ((i == 0 and -10 <= t[i] <= 10) or (i > 0 and t[i] > t[i-1])):
        t[i] = int(input((f"Donner l'élément n°{i} ? ")))

# séquence 3
a = int(input("Donner un entier ? "))

# séquence 4
i = -1
while True:
    i = i + 1
    if (i == n) or (t[i] > a):
        break
p = i

# séquence 5
print("p =", p)

"""
6
-2
1
5
7
12
26
"""