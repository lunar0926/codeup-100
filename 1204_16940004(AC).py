n = int(input())
if n >= 1 and n <= 20:
    if n == 1:
        print('1st')
    elif n == 2:
        print('2nd')
    elif n == 3:
        print('3rd')
    else:
        print('%dth'%n)

else: # 21~99
    s = str(n)
    if s[1] == '1':
        print('%dst' % n)
    elif s[1] == '2':
        print('%dnd' % n)
    elif s[1] == '3':
        print('%drd' % n)
    else:
        print('%dth' % n)
