n = float(input())
i = int(n) # 정수 부분
f = n - i # 실수 부분 6자리까지 
print(i)
if (f == 0):
    print(int(f))
f = '%.6f'%f
f = f.replace('0','')
f = f.replace('.','')
if ('-' in f):
    f = f.replace('-','')
print(f)


