a = int(input("a ? "))
b = int(input("b ? "))
cpt = 0
for i in range(a, b+1):
    u = i % 10
    d = (i // 10) % 10
    c = (i // 100) % 10
    m = i // 1000
    if u == 8:
        cpt += 1
    if d == 8:
        cpt += 1
    if c == 8:
        cpt += 1
    if m == 8:
        cpt += 1
print(cpt)