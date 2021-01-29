'''
최소공배수 활용
방문주기 문자열을 나눠서 int()

셋 다 같은 날에 모이는 것. 최소공배수가 되는 날. 
a,b,c로 n이 동시에 나누어 떨어지는 수 
'''
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
n = 0
while(True):
    n += 1
    if (n % a == 0 and n % b == 0 and n % c == 0):
        print(n)
        break
