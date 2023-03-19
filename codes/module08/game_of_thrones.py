from numpy import array


def saisie_entier(msg, mn, mx):
    valide = False
    while not valide:
        n = int(input(msg))
        valide = (mn <= n <= mx)
        if not valide:
            print("Give a number between", mn, "and", mx, ".")
    return n


def saisie_cat(msg):
    cat = ""
    while cat not in ["SW", "AR", "SH", "WE"]:
        cat = input(msg)
    return cat


def existe(val, t, n):
    tr = False
    i = 0
    while not tr and i < n:
        tr = t[i] == val
        i += 1
    return tr


def remplir(n):
    items = array([str]*n)
    categories = array([str]*n)
    prices = array([int()]*n)
    for i in range(n):
        print("Item n°", i)
        valide = False
        while not valide:
            items[i] = input("Name ? ")
            valide = len(items[i]) >= 3 and not existe(items[i], items, i)

        categories[i] = saisie_cat("Category ? ")

        prices[i] = saisie_entier("Price ? ", 0, 1000000)
    return items, categories, prices


def affordables(budget, catsel, items, categories, prices, n):
    ic = 0
    print("Affordable items")
    for i in range(n):
        if catsel == categories[i] and budget >= prices[i]:
            print("Item:", items[i], " - Price:", prices[i])
            ic += 1
    if ic == 0:
        print("No items.")

# PP
n = saisie_entier("Number of items [2, 50] ? ", 2, 50)
items, categories, prices = remplir(n)
budget = saisie_entier("Your budget ? ", 20, 300)
catsel = saisie_cat("Select a category ? ")
affordables(budget, catsel, items, categories, prices, n)