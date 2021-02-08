a, b = map(int, input().split())
nList = [a, b]
nList.sort()
result = 0
sList = ''
count = 0
while(True):
    count += 1
    if nList[0] <= nList[1]:
        if nList[0] % 2 == 0: # 짝수일 때
            result -= nList[0]
            sList = sList + '-' + str(nList[0])
        else:
            result += nList[0]
            if count == 1: # 첫 번째 짝수는 부호 안 나오도록
                sList += str(nList[0])
            else:
                sList = sList + '+' + str(nList[0])
        nList[0] += 1
    else:
        break
print('%s=%d'%(sList, result))

