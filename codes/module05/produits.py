a = int(input("Donner a ? "))
b = int(input("Donner b ? "))
s = 0
for i in range(abs(b)):
    s = s + a
if b < 0:
    s = -s
print(a, "×", b, "=", s)