n = input()
zip = []
if len(n) == 1:
    zip.append(n)
    zip.append('0')
    zip = zip[0] + zip[1]
    zip = int(zip) * 2
elif len(n) == 2:
    zip.append(n[1])
    zip.append(n[0])
    zip = zip[0] + zip[1]
    zip = int(zip) * 2

if zip >= 100:
    result = zip - 100
    print(result)
else:
    result = zip
    print(result)
if result <= 50:
    print('GOOD')
else:
    print('OH MY GOD')
