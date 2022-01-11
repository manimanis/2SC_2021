for i in range(1000, 9999, 5):
    u = i % 10
    d = (i // 10) % 10
    c = (i // 100) % 10
    m = (i // 1000) % 10
    s = u+d+c+m
    if c != 0 and m > c and d*2 == c and s >= 22:
        print(i)