'''
입력 1. 횟수n 2. 무작위로 n개의 번호를 부름.
입력값을 변수로 받고 n개의 리스트 만들기 
무작위 값에 따라서 순차적으로 해당 리스트 + 1
무작위 값도 리스트로 만들어서(문자열 상태) 받고 각각의 요소를 
정수로 변환해서 리스트의 해당 값에 +1 
리스트는 0부터 시작하는 것 참고 
출력은 리스트 전체가 나오도록 
'''
n = int(input())
randomList = input().split() # 문자열로 split해서 먼저 받기
nList = [0 for i in range(23)] # 23개의 리스트 생성. 23개는 고정 
for i in randomList:
    i = int(i)
    nList[i-1] += 1 # 해당 번호에서 1씩 더해주기
for j in nList:
    print(j, end =' ') # 줄바꿈없이 리스트 요소 나열 




