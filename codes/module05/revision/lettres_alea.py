from random import randint
n = int(input("Nombre de lettres ? "))
ch = ""
for i in range(n):
    ch = ch + chr(65 + randint(0, 25))
print(ch)