from random import randint, seed

n = 21
a = [randint(0, 100) for i in range(n)]
b = [randint(0, 100) for i in range(n)]
print(a)
print(b)

inter = [0]*n
ni = 0
for i in range(n):
    p, j = -1, 0
    while p == -1 and j < n:
        if a[i] == b[j]:
            p = j
        else:
            j += 1
    if p != -1:
        inter[ni] = a[i]
        ni += 1

print(inter[:ni])