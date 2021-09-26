dt = input("Entrer une date (jj/mm/aaaa) ? ")

j = int(dt[:2])
m = int(dt[3:5])
a = int(dt[6:])

if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    nbj = 31
elif m == 4 or m == 6 or m == 9 or m == 11:
    nbj = 30
else:
    nbj = 28

j = j + 1
if j > nbj:
    j = 1
    m = m + 1
if m > 12:
    m = 1
    a = a + 1

print("Lendemain =", j, "/", m, "/", a)