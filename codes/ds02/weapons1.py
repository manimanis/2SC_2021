from numpy import array

n = -1
while n < 2 or n > 30:
    n = int(input("Number of items [2, 30]? "))

cats = ['SW', 'AR', 'SH', 'WE']

items = array([str]*n)
categories = array(["XX"]*n)
prices = array([int()]*n)
for i in range(n):
    print("-- Item", i)
    items[i] = ""
    while len(items[i]) < 3:
        items[i] = input("Name? ")
    while categories[i] not in cats:
        categories[i] = input("Category [SW, AR, SH, WE]? ")
    prices[i] = -1
    while prices[i] < 0:
        prices[i] = int(input("Price (>=0)? "))

budget = -1
while budget < 0:
    budget = int(input("Your budget? "))

catsel = ''
while catsel not in cats:
    catsel  = input("Select a category? ")

print("Affordable items:")
ic = 0
for i in range(n):
    if categories[i] == catsel and prices[i] < budget:
        print("Item:", items[i], "- Price:", prices[i])
        ic = ic + 1
if ic == 0:
    print("No items.")