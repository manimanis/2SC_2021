from random import randint


def NombreSecret():
    a = 0
    b = 0
    c = 0
    while not (a != b != c):
        a = randint(1, 9)
        b = randint(0, 9)
        c = randint(0, 9)
    n = a * 100 + b * 10 + c
    return n


def Saisie():
    n = 0
    while n < 100 or n > 999:
        n = int(input(" ? "))
    return n


def VacheTaureau(n, s):
    ch1 = str(n)
    ch2 = str(s)
    res = ""
    for i in range(len(ch2)):
        if ch1[i] == ch2[i]:
            res = res + "T"
        elif ch2.find(ch1[i]) == -1:
            res = res + "-"
        else:
            res = res + "V"
    return res


# PP
secret = NombreSecret()
essai = 0
ch = ""
while ch != "TTT" and essai != 6:
    essai = essai + 1
    print("Essai", essai, end="")
    n = Saisie()
    ch = VacheTaureau(n, secret)
    print(ch)
if ch == "TTT":
    print("Bravo, vous avez deviné")
else:
    print("Le nombre cherché est", secret, ".")