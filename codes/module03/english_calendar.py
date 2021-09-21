df = input("Date au format jj/mm/aaaa ? ")
de = df[3:6] + df[:3] + df[6:]
print(df, "is", de, "in english calendar.")