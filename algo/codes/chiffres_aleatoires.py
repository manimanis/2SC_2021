from random import randint

seq = ""
for i in range(5):
    seq = seq + str(randint(0, 9))
print(seq)

seq = ""
while len(seq) < 2 or seq[-2] != seq[-1]:
    seq = seq + str(randint(0, 9))
print(seq)

seq = ""
for i in range(5):
    existe = True
    while existe:
        car = str(randint(0, 9))
        existe = seq.find(car) != -1
    seq = seq + car
print(seq)