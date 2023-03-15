def chiffre(c):
    if c == 'M':
        return 1000
    if c == 'D':
        return 500
    if c == 'C':
        return 100
    if c == 'L':
        return 50
    if c == 'X':
        return 10
    if c == 'V':
        return 5
    if c == 'I':
        return 1
    return 0


def convert_romain(ch):
    i = 0
    s = 0
    while i < len(ch):
        if i + 1 < len(ch) and chiffre(ch[i]) < chiffre(ch[i+1]):
            s = s + chiffre(ch[i+1]) - chiffre(ch[i])
            i = i + 1
        else:
            s = s + chiffre(ch[i])
        i = i + 1
    return s

rom = input("Donner un nombre romain : ")
dec = convert_romain(rom)
print(f"{rom} => {dec}")