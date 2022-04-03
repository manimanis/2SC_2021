from random import randint, seed

n = 21
t1 = [randint(0, 100) for i in range(n)]
print(t1)

t2 = [0]*n
i, j = 0, n-1
for k in range(n):
    if k % 2 == 0:
        t2[i] = t1[k]
        i += 1
    else:
        t2[j] = t1[k]
        j -= 1

print(t2)