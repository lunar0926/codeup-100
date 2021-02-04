# 정수를 문자열로 바꿔서 마지막 자리가 '0'인지를 조건식으로 확인
y, m, d = map(int, input().split())
result = y + m + d
s = str(result)
if len(s) == 5:
    hundred = int(s[2])
    if hundred % 2 == 0:
        print('대박')
    else:
        print('그럭저럭')
elif len(s) == 4:
    hundred = int(s[1])
    if hundred % 2 == 0:
        print('대박')
    else:
        print('그럭저럭')
elif len(s) == 3:
    hundred = int(s[0])
    if hundred % 2 == 0:
        print('대박')
    else:
        print('그럭저럭')

