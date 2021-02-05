a, b, c, d, e, f, g = map(int, input().split())
lotto = [a, b, c, d, e, f] # 보너스 번호 g는 제외
A, B, C, D, E, F = map(int, input().split())
my = [A, B, C, D, E, F]
n = 0 # 일치 개수
bonus = 0
for i in my:
    for j in lotto:
        if i == j:
            n += 1
for i in my:
    if i == g: # 보너스 번호와 일치
        bonus += 1
if n == 6:
    print(1)
elif n == 5:
    if bonus == 1:
        print(2)
    else:
        print(3)
elif n == 4:
    print(4)
elif n == 3:
    print(5)
else:
    print(0)

