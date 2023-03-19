def codebarre():
    cab = ""
    while not (len(cab) == 13 and cab.isdigit()):
        cab = input("Code EAN13 ? ")
    return cab


def est_valide(cab):
    q = cab[:-1]
    cc = cab[-1]
    s = 0
    for i in range(len(q)):
        s += int(q[i])
        if i % 2 != 0:
            s += 2 * int(q[i])
    r = s % 10
    if r != 0:
        p = str(10 - r)
    else:
        p = "0"
    return p == cc


# PP
cab = codebarre()
if est_valide(cab):
    print("Code EAN13 valide.")
else:
    print("Code EAN13 invalide.")
    
