# 소수 1하고 지만 됨
# 리스트를 만들고 리스트가 두 개가 되면 반복을 끝내기
# n의 약수임과 동시에 소수인 수를 구하기
# 두 소수의 곱인지도 확인하기
n = int(input())
primeList = []
for i in range(2, n):
    if n % i == 0: # n의 약수인지 확인
        primeList.append(i)
    else:
        continue
    # 소수가 2개인지 확인
    if len(primeList) == 2:
        break
# 해당 수가 소수인지 확인
for i in primeList:
    for j in range(2, i):
        if i % j == 0:
            print('wrong number')
            quit()
if len(primeList) == 2 and n == primeList[0] * primeList[1]:
    print('%d %d'%(primeList[0], primeList[1]))
else:
    print('wrong number')
