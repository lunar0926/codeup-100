'''
무작위로 번호를 부름 
두번째 줄은 input().split()으로 문자열 리스트로 받기 
각 리스트 요소를 정수로 변환 
리스트 내에서 가장 작은 수를 찾기 
min 이라는 변수를 선언 
두 수를 비교하는 방식으로 min을 찾아나가기
'''
n = int(input())
nList = input().split() # 문자열 리스트로 받기 
for i in range(0, n):
    nList[i] = int(nList[i])
min = nList[0]
for j in range(0, n):
    if nList[j] < min:
        min = nList[j]
print(min)
        

