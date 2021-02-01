'''
출력 mb 단위로 출력 둘째 자리까지 출력. 공백 MB
bit단위로 용량이 구해짐. 
1mb = 1024 * 8 * 1024

'''
w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)
bit = w * h * b
mb = bit / (1024 * 1024 * 8)
print('%.2f MB'%mb)

