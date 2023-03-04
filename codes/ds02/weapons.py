from random import randint

items = [
    ("The Sword of Jon Snow", "SW", 239),
    ("Sword of Arya Stark", "SW", 179),
    ("Widow’s Wail Sword", "SW", 649),
    ("Dragon Leather Bracers Set", "AR", 38),
    ("The Helm of Loras Tyrell", "AR", 249),
    ("Stark Infantry Shield", "SH", 257),
    ("Lannister Shield", "SH", 275),
    ("The Red Viper’s Spear", "WE", 299)
]
categories = ['SW', 'AR', 'SH', 'WE']

for item, category, price in items:
    print(item)
    print(category)
    print(price)

gold = randint(100, 400)
print("Player's gold?", gold)

n = len(items)
print("Number of items [2, 30] ?", n)

for i in range(n):
    print("-- Item", i)
    print("Item name?", items[i][0])
    print("Item category [SW, AR, SH, WE]?", items[i][1])
    print("Item price >=0 ?", items[i][2])

category = categories[randint(0, len(categories) - 1)]
print("Select a category?", category)

print("Affordable items:")
items_count = 0
for i in range(n):
    if items[i][1] == category and items[i][2] <= gold:
        print(items[i][0], "- Price:", items[i][2])
        items_count += 1
if items_count == 0:
    print("No items")