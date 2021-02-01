'''
hz, bit, 모노스테레오채널, 녹음시간 순
곱하면 비트 
MB 단위로 나와야 함.
1024 * 8 bit = 1 kb
1024 * 8 bit * 1024 = 1 mb

결과값에 위 1mb를 나누면 mb단위로 나옴.

출력할 때는 소수점 아래 첫째 자리까지. 공백 MB
'%.1f MB'%
'''
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
bit = h * b * c * s
mb = bit / (1024 * 1024 * 8)
print('%.1f MB'%mb)
