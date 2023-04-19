n1 = 0
while n1 <= 0:
    n1 = int(input("Donner n1 > 0 ? "))

n2 = 0
while n2 <= 0:
    n2 = int(input("Donner n2 > 0 ? "))

ch1 = str(n1)
c1 = ""
for i in range(10):
    v = str(i)
    if v in ch1:
        c1 += v

ch2 = str(n2)
c2 = ""
for i in range(10):
    v = str(i)
    if v in ch2:
        c2 += v

if c1 == c2:
    print(n1, "et", n2, "sont frères")
else:
    print(n1, "et", n2, "ne sont pas frères")