def increase(p):
    global counter
    counter = counter + p

def decrease(p):
    increase(-p)

counter = 7
for i in range(5):
    if i % 4 == 0:
        increase(1)
    elif i % 4 == 1:
        decrease(3)
    elif i % 4 == 2:
        increase(5)
    else:
        decrease(7)
print(counter)