a, b = map(int, input().split())
nList = []

plus1 = a + b
nList.append(plus1)
plus2 = b + a
nList.append(plus2)

minus1 = a - b
nList.append(minus1)
minus2 = b - a
nList.append(minus2)

multiply1 = a * b
nList.append(multiply1)
multiply2 = b * a
nList.append(multiply2)

divide1 = a / b
nList.append(divide1)
divide2 = b / a
nList.append(divide2)

power1 = a ** b
nList.append(power1)
power2 = b ** a
nList.append(power2)

nList.sort()
print('%.6f'%nList[9])
