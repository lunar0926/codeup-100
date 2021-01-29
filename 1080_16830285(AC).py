'''
입력값 n
1부터 n까지 더하기 sum 
반복문 i in range(n)

if sum >= n:
    print(i)
'''
n = int(input())
sum = 0
for i in range(1, n):
    sum += i
    if sum >= n:
        print(i)
        break
