menu = [None, 400, 340, 170, 100, 70]
a, b = map(int, input().split())
a = menu[a]
b = menu[b]
if a + b > 500:
    print('angry')
else:
    print('no angry')
