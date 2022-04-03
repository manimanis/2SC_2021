from random import randint, seed

n = 21
t = [randint(0, 100) for i in range(n)]
print(t)

pa, im = 0, n-1
while im >= pa:
    while pa < n and t[pa] % 2 == 0:
        pa += 1
    while im >= pa and t[im] % 2 != 0:
        im -= 1
    if im > pa:
        t[pa], t[im] = t[im], t[pa]
        pa += 1
        im -= 1

print(t[:pa], t[pa:])