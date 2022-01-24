from random import randint
n = int(input("Nombre de chiffres ? "))
ch = ""
for i in range(n):
    ch = ch + chr(48 + randint(0, 9))
print(ch)