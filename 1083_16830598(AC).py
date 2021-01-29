'''
조건문으로 3, 6, 9에 해당될 때 'X'를 출력

'''
n = int(input())
for i in range(1, n+1):
    if i == 3 or i == 6 or i == 9:
        print('X', end = ' ')
    else:
        print(i, end =' ')
