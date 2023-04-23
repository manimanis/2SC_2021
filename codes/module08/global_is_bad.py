# global are bad
from random import randint
from numpy import array

def chiffres_distints(n):
    global i
    t = array([0]*n)
    i = 0
    while i < n:
        distinct = False
        while not distinct:
            chiffre = randint(0, 9)
            distinct = not existe(chiffre, t, i)
        t[i] = chiffre
        i = i + 1
    return t

def existe(chiffre, t, n):
    global i
    i = n - 1
    trouve = False
    while not trouve and i >= 0:
        trouve = t[i] == chiffre
        i = i - 1
    return trouve

print(chiffres_distints(8))
