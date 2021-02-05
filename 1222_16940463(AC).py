t, one, two = map(int, input().split())
while(True):
    if t < 90:
        one += 1
        t += 5
    else:
        break
if one > two:
    print('win')
elif one == two:
    print('same')
elif one < two:
    print('lose')
