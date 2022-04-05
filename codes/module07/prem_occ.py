from random import randint, seed

n = 21
t1 = [randint(1, 19) for i in range(n)]
print(t1)

k = -1
for i in range(n):
    p, j = -1, 0
    while p == -1 and j < i:
        if t1[j] == t1[i]:
            p = j
        else:
            j += 1
    if p == -1:
        k += 1
        t1[k] = t1[i]

n = k+1
print(t1[:n])