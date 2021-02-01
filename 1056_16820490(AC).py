# 값이 같을 때에만 0출력 나머지는 1출력
a, b = input().split()
a = int(a)
b = int(b)
if (a == 0 and b == 0) or (a == 1 and b == 1):
    print(0)
else:
    print(1)
