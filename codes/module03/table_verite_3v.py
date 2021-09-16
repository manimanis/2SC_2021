bool_val = [False, True]
for a in bool_val:
    for b in bool_val:
        for c in bool_val:
            print(a, b, c, not a or b and c, (not a) or (b and c), not ((a or b) and c), (not (a or b)) and c)
