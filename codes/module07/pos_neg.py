from random import randint, seed

n = 21
t = [randint(-50, 50) for i in range(n)]
print(t)

po, ne = 0, n-1
while ne >= po:
    while po < n and t[po] >= 0:
        po += 1
    while ne >= po and t[ne] < 0:
        ne -= 1
    if ne > po:
        t[po], t[ne] = t[ne], t[po]
        po += 1
        ne -= 1

print(t[:po], t[po:])