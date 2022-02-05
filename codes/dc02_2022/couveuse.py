from random import randint

no = int(input("Donner le nombre d'oeufs ? "))

oeufs = "pppppppxxx"
seq = ""
for i in range(no):
    seq = seq + oeufs[randint(0, len(oeufs) - 1)]
print(seq)

# ch = "1000100010110001"
# ch2 = ""
# for i in range(len(ch)):
#     if ch[i] == "1":
#         ch2 = ch2 + ch[i]
# print(ch2)

seq2 = ""
for i in range(no):
    if seq[i] == "p":
        seq2 = seq2 + seq[i]
np = len(seq2)
print("Nombre de poussins vifs :", np , "/", no)

seq3 = ""
for i in range(np):
    tp = randint(0, 1)
    if tp == 0:
        seq3 = seq3 + "P"
    else:
        seq3 = seq3 + "C"
print(seq3)