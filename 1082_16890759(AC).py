n = int(input(), 16)  # 입력받은 10진수
s1 = format(n, 'x').upper()  # 출력용
for i in range(1, 16):
    s2 = format(i, 'x').upper()  # 출력용
    result = n * i
    s3 = format(result, 'x').upper()
    print('%s*%s=%s' % (s1, s2, s3))



