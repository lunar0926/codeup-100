n = int(input())

if n < 0:
    print('minus')
    if n % 2 == 0:
        print('even')
    else: 
        print('odd')
else:
    print('plus')
    if n % 2 == 0:
        print('even')
    else:
        print('odd')

