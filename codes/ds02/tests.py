ch = "Israa Amor Yassmine Adem"
ch1 = ""
for i in range(2, len(ch)):
    if i == 2 or ch[i-3] == " ":
        ch1 += ch[i]
print(ch1)

s = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 3 == 0:
            s += 1
print(s)

ch = "Ahmed Eya"
ch1 = "oiyeau"
ch2 = ""
for i in range(len(ch)):
  if ch1.find(ch[i]) != -1:
    ch2 = ch2 + ch[i]
print(ch2)

ch = "abdoud"
ch1 = ""
for i in range(len(ch)-1, -1, -1):
    if ord(ch[i]) - 97 > 10:
        ch1 = ch1 + ch[i].upper()
    else:
        ch1 = ch1 + ch[i]
print(ch1)

def prim1(n):
    i = 2
    while i < (n // 2) and n % i != 0:
        i += 1
    test = i == n // 2 and n > 1
    print(test)
prim1(11)
prim1(12)

def prim2(n):
    test = True
    i = 1
    while True:
        i += 1
        test = n % i == 0
        if not test or i == n // 2:
            break
    print(test)
prim2(11)
prim2(12)

def prim3(n):
    test = True
    i = 1
    while i <= n // 2:
        if n % i == 0:
            test = False
        else:
            i += 1
    print(test)
#prim3(11)
#prim3(12) # boucle sans fin

def prim4(n):
    s = 0
    for i in range(1, n+1):
        if n % i == 0:
            s += 1
    test = s == 2
    print(test)
prim4(11)
prim4(12)
