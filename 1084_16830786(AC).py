'''
출력하고 나면 count++
0부터 n-1까지 range(n)
입력값은 문자열을 split()
각각 정수로 저장 r, g, b
중첩 반복문으로 가장 내부에 있는 반복문에서 출력, count
'''
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print('{0} {1} {2}'.format(i, j, k))
            count += 1
print(count)
            
