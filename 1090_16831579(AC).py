'''
등비수열 ar^n-1 
a * r ** (n-1)
시작 값, 등비, 몇 번째
'''
a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)
print(a * r ** (n-1))

