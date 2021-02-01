'''
등차수열 식 이용 a + (n-1)d
시작 값, 등차, 몇 번째인지
'''
a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)
print(a+(n-1)*d)
