# Saisie de deux nombres strictement positifs
n = 0
while n <= 0:
    n = int(input("Donner n ? "))
m = 0
while m <= 0:
    m = int(input("Donner m ? "))
# calcul de la somme diviseurs de n
sn = 0
for i in range(1, n // 2+1):
    if n % i == 0:
        sn = sn + i
# calcul de la somme diviseurs de m
sm = 0
for i in range(1, m//2 + 1):
    if m % i == 0:
        sm = sm + i
# Affichage du résultat
if (n == sm) and (m == sn):
    print(n, "et", m, "sont amicaux.")
else:
    print(n, "et", m, "ne sont pas amicaux.")
