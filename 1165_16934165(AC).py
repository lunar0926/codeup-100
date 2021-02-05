t, g = map(int, input().split())
while(True):
    if t < 90:
        g += 1
        t += 5
    else:
        break
print(g)
