h, m = map(int, input().split())
if m < 30:
    if h == 0:
        h = 24
    h -= 1
    m += 30
    print(h, end=' ')
    print(m)
else:
    m -= 30
    print(h, end=' ')
    print(m)
