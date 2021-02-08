a, b = map(float, input().split())
while(True):
    if a <= b:
        print('%.2f'%a, end = ' ')
        a += 0.01
    else:
        break
