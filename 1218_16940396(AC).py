a, b, c = map(int, input().split())
t = [a, b, c] # triangle
t.sort()
if t[2] < t[0] + t[1]: # 삼각형 중에서
    if t[0] == t[1] == t[2]:
        print('정삼각형')
    elif (t[0] == t[1] and t[1] != t[2]) or (t[0] == t[2] and t[2] != t[1]) or (t[1] == t[2] and t[2] != t[0]):
        print('이등변삼각형')
    elif t[0] ** 2 + t[1] ** 2 == t[2] ** 2:
        print('직각삼각형')
    else:
        print('삼각형')
else:
    print('삼각형아님')

