a = -1
while not 0 < a <= 100:
    a = int(input("Donner 0 < a <= 100? "))
b = -1
while not a <= b <= 100:
    b = int(input(f"Donner {a} <= b <= 100? "))
print((a + b) / 2)