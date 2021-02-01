# 주사위 2개 입력받기 a, b
# 반복문으로 출력. 이때 외부는 a주사위 내부는 b주사위가 줄바꾸지 않고 출력
a, b = input().split()
a = int(a)
b = int(b)
for i in range(1, a+1):
    for j in range(1, b+1):
        print('{} {}'.format(i, j))
        
