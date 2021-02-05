str = input()
if str.find('+') != -1:
    a, b = map(int, str.split('+'))
    print(a + b)
elif str.find('-') != -1:
    a, b = map(int, str.split('-'))
    print(a - b)
elif str.find('*') != -1:
    a, b = map(int, str.split('*'))
    print(a * b)
elif str.find('/') != -1:
    a, b = map(int, str.split('/'))
    print('%.2f'%(a / b))

