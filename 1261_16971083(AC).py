a, b, c, d, e, f, g, h, i, j = map(int, input().split())
nList = [a, b, c, d, e, f, g, h, i, j]
n = 0 # 5의 배수를 찾으면 +1
for i in nList:
    if i % 5 == 0:
        print(i)
        n += 1
        break
    else:
        continue
if n == 0:
    print(0)


