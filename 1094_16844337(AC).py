'''
무작위로 번호를 부름. 이 무작위 번호를 다시 거꾸로 출력
두 개의 입력을 받음. 
두 번째 입력은 문자열 리스트(split())로 받아서 reverse로 거꾸로 
출력할 때는 각 요소를 정수로 바꾼 뒤에 줄바꿈하지 않고 출력
'''
n = int(input())
nList = input().split()
nList.reverse()
for i in nList:
    i = int(i)
    print(i, end = ' ')

