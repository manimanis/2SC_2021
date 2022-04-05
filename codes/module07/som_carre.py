from random import randint, seed

n = 21
t1 = [randint(100, 999) for i in range(n)]
print(t1)

t2 = [0] * n
for i in range(n):
    v = t1[i]
    s = 0
    while v != 0:
        s += (v % 10)*(v % 10)
        v //= 10
    t2[i] = s

print(t2)